from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from diary.models import *
from django.db.models import Q
import json
from common.utils import model_to_json, collection_to_json
from datetime import datetime, timedelta
# Create your views here.


@login_required
def home(request, i = 10):
	info = dict()

	try:
		events = Event.objects.filter(calender = Calender.objects.filter(owner = request.user.username), active = 0, end__gt = datetime.now()).order_by('start')[:i]
		info["status"] = 0
		info["events"] = collection_to_json(events)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def day(request, i = 0):
	info = dict()
	info["sf"] = i
	try:

		day = Day.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'content' in request.POST:
				day.content = request.POST['content']
			if 'attr1' in request.POST:
				day.attr1 = request.POST['attr1'],
			if 'attr2' in request.POST:
				day.attr2 = request.POST['attr2'],
			day.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		info["status"] = 0
		info["day"] = model_to_json(day)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def delCalender(request,  i = -1):
	info = dict()

	try:
		calender = Calender.objects.filter(pk = i)[0]
		if calender.priority == 0:
			info["status"] = 1
			info["msg"] = "defaultCalender"
		else:
			calender.delete()
			info["status"] = 0
		info["delCalender"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def delEvent(request, i = -1):
	info = dict()

	try:
		event = Event.objects.filter(pk = i)[0]
		if event.active == 0:
			event.active = 1
			event.save()
			info["active"] = 1
		else:
			event.delete()
			info["active"] = 2
		info["status"] = 0
		info["delEvent"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def delDay(request, i = -1):
	info = dict()

	try:
		day = Day.objects.filter(pk = i)[0]
		day.delete()
		info["status"] = 0
		info["delDay"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def makeDefaultCalender(request, i = 0):
	info = dict()

	try:
		oldCalender = Calender.objects.filter(owner = request.user.username, priority = 0)[0]
		newCalender = Calender.objects.filter(pk = i)[0]
		oldCalender.priority = newCalender.priority
		newCalender.priority = 0
		oldCalender.save()
		newCalender.save()
		info["status"] = 0
		info["oldCalender"] = model_to_json(oldCalender)
		info["newCalender"] = model_to_json(newCalender)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def newCalender(request):
	info = dict()

	try:
		calenders = Calender.objects.filter(owner = request.user.username)
		if not calenders:
			name = "Default Calender"
			priority = 0
		else:
			name = request.POST.get('name', 'Calender ' + str(Calender.objects.filter(owner = request.user.username).count() + 1))
			priority = request.POST.get('priority', 1)

		calender = Calender.objects.create(
					owner = request.user.username,
					name = name,
					priority = priority,
					active = request.POST.get('active', 0),
					attr1 = request.POST.get('attr1', ""),
					attr2 = request.POST.get('attr2', "")
				)
		calender.save()
		info["status"] = 0
		info["newCalender"] = calender.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def newEvent(request):
	info = dict()

	try:
		if 'calender' in request.POST:
			calender = Calender.objects.filter(owner = request.user.username, calender = request.POST['calender'])[0]
		else:
			calender = Calender.objects.filter(owner = request.user.username, priority = 0)[0]
		event = Event.objects.create(
					name = request.POST.get('name', 'Untitled ' + str(Event.objects.filter(calender = calender).count() + 1)),
					calender = calender,
					start = request.POST.get('start', datetime.now()),
					end = request.POST.get('end', datetime.now()),
					remind = request.POST.get('remind', 0),
					reminder = request.POST.get('reminder', datetime.now()),
					priority = request.POST.get('priority', 0),
					active = request.POST.get('active', 0),
					attr1 = request.POST.get('attr1', ""),
					attr2 = request.POST.get('attr2', ""),
					desc = request.POST.get('content', ""),
				)
		event.save()
		info["status"] = 0
		info["newEvent"] = event.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def newDay(request):
	info = dict()

	try:
		date = request.POST.get('date', datetime.now().date())
		if Day.objects.filter(date = date).count():
			return day(request, Day.objects.filter(date = date)[0].pk)
		else:
			nDay = Day.objects.create(
						owner = request.user.username,
						date = date,
						attr1 = request.POST.get('attr1', ""),
						attr2 = request.POST.get('attr2', "")
					)
			events = Event.objects.filter(calender = Calender.objects.filter(owner = request.user.username), start__lte = datetime.combine(date + timedelta(days=1), datetime.min.time()), end__gte = datetime.combine(date, datetime.min.time())).order_by('priority','start')
			info["c"] = events.count()
			for event in events:
				nDay.content += event.desc + "\n"
			nDay.save()
			info["status"] = 0
			info["newDay"] = nDay.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def calender(request, i = 0):
	info = dict()

	try:
		calender = Calender.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in request.POST:
				calender.name = request.POST['name']
			if 'priority' in request.POST:
				if calender.priority != 0 and request.POST['priority'] !=0:
					calender.priority = request.POST['priority']
			if 'attr1' in request.POST:
				calender.attr1 = request.POST['attr1'],
			if 'attr2' in request.POST:
				calender.attr2 = request.POST['attr2'],
			calender.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"
			mode = request.GET.get('mode', 'month')
			ref = request.GET.get('ref', datetime.now())
			if mode == 'time':
				childEvents = Event.objects.filter(calender = calender.pk, start__lte = datetime.combine(ref.date(), datetime.max.time()), end__gte = ref).order_by('start')
			elif mode == 'day':
				childEvents = Event.objects.filter(calender = calender.pk, start__lte = datetime.combine(ref.date(), datetime.max.time()), end__gte = datetime.combine(ref.date(), datetime.min.time())).order_by('start')
			elif mode == 'week':
				childEvents = Event.objects.filter(calender = calender.pk, start__lte = datetime.combine(ref.date() + timedelta(days=7), datetime.min.time()), end__gte = datetime.combine(ref.date(), datetime.min.time())).order_by('start')
			else:
				childEvents = Event.objects.filter(calender = calender.pk, start__month = ref.month, end__month = ref.month, start__year = ref.year, end__year = ref.year).order_by('start')
			info["childEvents"] = collection_to_json(childEvents)

		info["status"] = 0
		info["calender"] = model_to_json(calender)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def calenders(request):
	info = dict()

	try:
		calenders = Calender.objects.filter(owner = request.user.username).order_by('priority', 'name')
		info["status"] = 0
		info["calenders"] = collection_to_json(calenders)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def event(request, i = 0):
	info = dict()

	try:
		event = Event.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in request.POST:
				event.name = request.POST['name']
			if 'calender' in request.POST:
				event.calender = request.POST['calender']
			if 'start' in request.POST:
				event.start = request.POST['start']
			if 'end' in request.POST:
				event.end = request.POST['end']
			if 'remind' in request.POST:
				event.remind = request.POST['remind']
			if 'reminder' in request.POST:
				event.reminder = request.POST['reminder']
			if 'priority' in request.POST:
				event.priority = request.POST['priority']
			if 'attr1' in request.POST:
				event.attr1 = request.POST['attr1'],
			if 'attr2' in request.POST:
				event.attr2 = request.POST['attr2'],
			if 'desc' in request.POST:
				event.desc = request.POST['desc']
			event.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		info["status"] = 0
		info["event"] = model_to_json(event)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def restoreEvent(request, i = -1):
	info = dict()

	try:
		event = Event.objects.filter(pk = i)[0]
		event.active = 0
		event.save()
		info["active"] = 0
		info["status"] = 0
		info["restoreEvent"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def trash(request):
	info = dict()

	try:
		events = Event.objects.filter(owner = request.user.username, active = 1).order_by('-updated')
		info["status"] = 0
		info["events"] = collection_to_json(events)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))
