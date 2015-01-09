from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from notes.models import *
import json
from common.utils import model_to_json, collection_to_json
# Create your views here.


@login_required
def home(request, i = 10):
	info = dict()

	try:
		notes = Note.objects.filter(owner = request.user.username, active = 0).order_by('priority', '-updated')[:i]
		# info["status"] = 0
		info = collection_to_json(notes)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def delNote(request, i = -1):
	info = dict()

	try:
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
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newNote(request):
	info = dict()

	data = json.loads(request.body)
	try:
		note = Note.objects.create(
					owner = request.user.username,
					name = data.get('name', 'Note ' + str(Note.objects.filter(owner = request.user.username).count() + 1)),
					context = data.get('context', 0),
					active = data.get('active', 0),
					priority = data.get('priority', 0),
					attr1 = data.get('attr1', ""),
					attr2 = data.get('attr2', ""),
					content = data.get('content', ""),
				)
		info["status"] = 0
		info["newNote"] = note.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def note(request, i = 0):
	info = dict()

	data = json.loads(request.body)
	try:
		note = Note.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in data:
				note.name = data['name']
			if 'priority' in data:
				note.priority = data['priority']
			if 'attr1' in data:
				note.attr1 = data['attr1'],
			if 'attr2' in data:
				note.attr2 = data['attr2'],
			if 'content' in data:
				note.content = data['content']
			note.save();
			info["status"] = 0
			info["msg"] = "CHANGED"
		else:
			info["status"] = 0
			info["msg"] = "NOCHANGE"
		info["note"] = model_to_json(note)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def restoreNote(request, i = -1):
	info = dict()

	try:
		note = Note.objects.filter(pk = i)[0]
		note.active = 0
		note.save()
		info["active"] = 0
		info["status"] = 0
		info["restoreNote"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def trash(request):
	info = dict()

	try:
		notes = Note.objects.filter(owner = request.user.username, active = 1).order_by('-updated')
		info["status"] = 0
		info["notes"] = collection_to_json(notes)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")
