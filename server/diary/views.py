from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from diary.models import *
import json
from common.utils import model_to_json, collection_to_json
from datetime import datetime, timedelta
# Create your views here.


@login_required
def home(request, i = 10):
	info = dict()

	try:
		events = Event.objects.filter(calender = Calender.objects.filter(owner = request.user.username), active = 0, end__gt = datetime.now()).order_by('start')[:i]
		info = collection_to_json(events)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def day(request, i = 0):
	info = dict()
	try:

		day = Day.objects.filter(pk = i)[0]

		if request.method == "POST":
			data = json.loads(request.body)
			if 'content' in data:
				day.content = data['content']
			if 'attr1' in data:
				day.attr1 = data['attr1'],
			if 'attr2' in data:
				day.attr2 = data['attr2'],
			day.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		info["status"] = 0
		info["day"] = model_to_json(day)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newCalender(request):
	info = dict()

	try:
		data = json.loads(request.body)
		calenders = Calender.objects.filter(owner = request.user.username)
		if not calenders:
			name = "Default Calender"
			priority = 0
		else:
			name = data.get('name', 'Calender ' + str(Calender.objects.filter(owner = request.user.username).count() + 1))
			priority = data.get('priority', 1)

		calender = Calender.objects.create(
					owner = request.user.username,
					name = name,
					priority = priority,
					active = data.get('active', 0),
					attr1 = data.get('attr1', ""),
					attr2 = data.get('attr2', "")
				)
		info["status"] = 0
		info["newCalender"] = calender.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newEvent(request):
	info = dict()

	try:
		data = json.loads(request.body)
		if 'calender' in data:
			calender = Calender.objects.filter(owner = request.user.username, calender = data['calender'])[0]
		else:
			calender = Calender.objects.filter(owner = request.user.username, priority = 0)[0]
		event = Event.objects.create(
					name = data.get('name', 'Untitled ' + str(Event.objects.filter(calender = calender).count() + 1)),
					calender = calender,
					start = data.get('start', datetime.now()),
					end = data.get('end', datetime.now()),
					remind = data.get('remind', 0),
					reminder = data.get('reminder', datetime.now()),
					priority = data.get('priority', 0),
					active = data.get('active', 0),
					attr1 = data.get('attr1', ""),
					attr2 = data.get('attr2', ""),
					desc = data.get('content', ""),
				)
		info["status"] = 0
		info["newEvent"] = event.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newDay(request):
	info = dict()

	try:
		data = json.loads(request.body)
		date = data.get('date', datetime.now().date())
		if Day.objects.filter(date = date).count():
			return day(request, Day.objects.filter(date = date)[0].pk)
		else:
			nDay = Day.objects.create(
						owner = request.user.username,
						date = date,
						attr1 = data.get('attr1', ""),
						attr2 = data.get('attr2', "")
					)
			events = Event.objects.filter(calender = Calender.objects.filter(owner = request.user.username), start__lte = datetime.combine(date + timedelta(days=1), datetime.min.time()), end__gte = datetime.combine(date, datetime.min.time())).order_by('priority','start')
			for event in events:
				nDay.content += event.desc + "\n"
			info["status"] = 0
			info["newDay"] = nDay.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def calender(request, i = 0):
	info = dict()

	try:
		data = json.loads(request.body)
		calender = Calender.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in data:
				calender.name = data['name']
			if 'priority' in data:
				if calender.priority != 0 and data['priority'] !=0:
					calender.priority = data['priority']
			if 'attr1' in data:
				calender.attr1 = data['attr1'],
			if 'attr2' in data:
				calender.attr2 = data['attr2'],
			calender.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"
			mode = request.GET.get('mode', 'month')
			start = request.GET.get('start', datetime.now())
			end = request.GET.get('end', datetime.now() + timedelta(days = 1))
			childEvents = Event.objects.filter(calender = calender.pk, start__lte = end, end__gte = start).order_by('start')
			info["childEvents"] = collection_to_json(childEvents)

		info["status"] = 0
		info["calender"] = model_to_json(calender)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def event(request, i = 0):
	info = dict()

	try:
		event = Event.objects.filter(pk = i)[0]

		if request.method == "POST":
			data = json.loads(request.body)
			if 'name' in data:
				event.name = data['name']
			if 'calender' in data:
				event.calender = data['calender']
			if 'start' in data:
				event.start = data['start']
			if 'end' in data:
				event.end = data['end']
			if 'remind' in data:
				event.remind = data['remind']
			if 'reminder' in data:
				event.reminder = data['reminder']
			if 'priority' in data:
				event.priority = data['priority']
			if 'attr1' in data:
				event.attr1 = data['attr1'],
			if 'attr2' in data:
				event.attr2 = data['attr2'],
			if 'desc' in data:
				event.desc = data['desc']
			event.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		info["status"] = 0
		info["event"] = model_to_json(event)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")


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

	return HttpResponse(json.dumps(info), content_type="application/json")
