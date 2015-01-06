from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from diary.models import Event, Day
from pages.models import Page
from notes.models import Note
from tags.models import *
import json
from common.utils import model_to_json, collection_to_json
# Create your views here.


tagModels = {"Note": NoteTag, "Page": PageTag, "Event": EventTag, "Day": DayTag}
models = {"Note": Note, "Page": Page, "Event": Event, "Day": Day}


@login_required
def allTags(request, model = ''):
	info = dict()

	try:
		Tag = tagModels[model]
		tags = Tag.objects.filter(owner = request.user.username)
		info["status"] = 0
		info["tags"] = collection_to_json(tags)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newTag(request, model = ''):
	info = dict()

	try:
		Tag = tagModels[model]
		tag = Tag.objects.create(
					owner = request.user.username,
					name = request.POST.get('name', 'Tag ' + str(Tag.objects.filter(owner = request.user.username).count() + 1)),
					priority = request.POST.get('priority', 1),
					attr1 = request.POST.get('attr1', ""),
					attr2 = request.POST.get('attr2', "")
				)
		info["status"] = 0
		info["tag"] = tag.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def delTag(request, model = '', i = -1):
	info = dict()

	try:
		Tag = tagModels[model]
		tag = Tag.objects.filter(pk = i)[0]
		tag.delete()
		info["status"] = 0
		info["delTag"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def entities(request, model = '', i = -1):
	info = dict()

	try:
		Tag = tagModels[model]
		tag = Tag.objects.filter(pk = i)[0]
		info["status"] = 0
		info["entities"] = collection_to_json(tag.entities.all())
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def tags(request, model = '', i = -1):
	info = dict()

	try:
		Entity = models[model]
		entity = Entity.objects.filter(pk = i)[0]
		info["status"] = 0
		info["tags"] = collection_to_json(entity.tags.all())
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def tag(request, model = '', i = -1, j = -1):
	info = dict()

	try:
		Tag = tagModels[model]
		Entity = models[model]
		tag = Tag.objects.filter(pk = i)[0]
		entity = Entity.objects.filter(pk = j)[0]
		if tag.entities.filter(id = entity.id).exists():
			tag.entities.remove(entity)
			info["tag"] = 0
		else:
			info["tag"] = 1
			tag.entities.add(entity)
		info["status"] = 0
		info["entities"] = collection_to_json(tag.entities.all())
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")
