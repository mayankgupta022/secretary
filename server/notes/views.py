from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from notes.models import *
import json
from datetime import datetime
from common.utils import model_to_json, collection_to_json
# Create your views here.


@login_required
def home(request, i = 10):
	info = dict()

	notes = Note.objects.filter(owner = request.user.username, active = 0).order_by('-updated')[:i]
	info["status"] = 0
	info["notes"] = collection_to_json(notes)

	return HttpResponse(json.dumps(info))


@login_required
def delNote(request, i = -1):
	info = dict()

	note = Note.objects.filter(pk = i)[0]
	if note.active == 0:
		note.active = 1
		note.save()
		info["active"] = 1
	else:
		note.delete()
		info["active"] = 2
	info["status"] = 0
	info["delNote"] = i

	return HttpResponse(json.dumps(info))


@login_required
def newNote(request):
	info = dict()

	note = Note.objects.create(
				owner = request.user.username,
				name = request.POST.get('name', str(datetime.now())),
				context = request.POST.get('context', 0),
				active = request.POST.get('active', 0),
				priority = request.POST.get('priority', 0),
				attr1 = request.POST.get('attr1', ""),
				attr2 = request.POST.get('attr2', ""),
				content = request.POST.get('content', ""),
			)
	note.save()
	info["status"] = 0
	info["newNote"] = note.pk

	return HttpResponse(json.dumps(info))


@login_required
def note(request, i = 0):
	info = dict()

	note = Note.objects.filter(pk = i)[0]

	if request.method == "POST":
		if 'name' in request.POST:
			note.name = request.POST['name']
		if 'priority' in request.POST:
			note.priority = request.POST['priority']
		if 'attr1' in request.POST:
			note.attr1 = request.POST['attr1'],
		if 'attr2' in request.POST:
			note.attr2 = request.POST['attr2'],
		if 'content' in request.POST:
			note.content = request.POST['content']
		note.save();
		info["status"] = 0
		info["msg"] = "CHANGED"
	else:
		info["status"] = 1
		info["msg"] = "NOCHANGE"
	info["note"] = model_to_json(note)

	return HttpResponse(json.dumps(info))


@login_required
def restoreNote(request, i = -1):
	info = dict()

	note = Note.objects.filter(pk = i)[0]
	note.active = 0
	note.save()
	info["active"] = 0
	info["status"] = 0
	info["restoreNote"] = i

	return HttpResponse(json.dumps(info))


@login_required
def trash(request):
	info = dict()

	notes = Note.objects.filter(owner = request.user.username, active = 1).order_by('-updated')
	info["status"] = 0
	info["notes"] = collection_to_json(notes)

	return HttpResponse(json.dumps(info))