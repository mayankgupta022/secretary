from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pages.models import *
import json
from common.utils import model_to_json, collection_to_json
# Create your views here.


@login_required
def home(request, i = 10):
	info = dict()

	try:
		pages = Page.objects.filter(owner = request.user.username, active = 0).order_by('-updated')[:i]
		# info["status"] = 0
		info = collection_to_json(pages)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def delNotebook(request,  i = -1):
	info = dict()

	try:
		notebook = Notebook.objects.filter(pk = i)[0]
		if notebook.priority == 0:
			info["status"] = 1
			info["msg"] = "defaultNotebook"
		else:
			defaultNotebook = Notebook.objects.filter(owner = request.user.username, priority = 0)[0]
			pages = Page.objects.filter(notebook = i)
			for page in pages:
				page.notebook = defaultNotebook
				page.save()
			notebook.delete()
			info["status"] = 0
		info["delNotebook"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def delPage(request, i = -1):
	info = dict()

	try:
		page = Page.objects.filter(pk = i)[0]
		if page.active == 0:
			page.active = 1
			page.save()
			info["active"] = 1
		else:
			page.delete()
			info["active"] = 2
		info["status"] = 0
		info["delPage"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def delStack(request,  i = -1):
	info = dict()

	try:
		stack = Stack.objects.filter(pk = i)[0]
		notebooks = Notebook.objects.filter(stack = i)
		for notebook in notebooks:
			notebook.stack = 0
			notebook.save()
		stack.delete()
		info["status"] = 0
		info["delStack"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def makeDefaultNotebook(request, i = 0):
	info = dict()

	try:
		oldNotebook = Notebook.objects.filter(owner = request.user.username, priority = 0)[0]
		newNotebook = Notebook.objects.filter(pk = i)[0]
		oldNotebook.priority = newNotebook.priority
		newNotebook.priority = 0
		oldNotebook.save()
		newNotebook.save()
		info["status"] = 0
		info["oldNotebook"] = model_to_json(oldNotebook)
		info["newNotebook"] = model_to_json(newNotebook)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newNotebook(request):
	info = dict()

	data = json.loads(request.body)
	try:
		notebooks = Notebook.objects.filter(owner = request.user.username)
		if not notebooks:
			name = "Default Notebook"
			priority = 0
		else:
			name = data.get('name', 'Notebook ' + str(Notebook.objects.filter(owner = request.user.username).count() + 1))
			priority = data.get('priority', 1)

		notebook = Notebook.objects.create(
					owner = request.user.username,
					name = name,
					stack = data.get('stack', 0),
					priority = priority,
					attr1 = data.get('attr1', ""),
					attr2 = data.get('attr2', "")
				)
		info["status"] = 0
		info["newNotebook"] = notebook.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newPage(request):
	info = dict()

	data = json.loads(request.body)
	try:
		if 'notebook' in data:
			notebook = Notebook.objects.filter(owner = request.user.username, notebook = data['notebook'])[0]
		else:
			notebook = Notebook.objects.filter(owner = request.user.username, priority = 0)[0]
		page = Page.objects.create(
					owner = request.user.username,
					name = data.get('name', 'Untitled ' + str(Page.objects.filter(owner = request.user.username).count() + 1)),
					notebook = notebook,
					context = data.get('context', 0),
					active = data.get('active', 0),
					priority = data.get('priority', 0),
					attr1 = data.get('attr1', ""),
					attr2 = data.get('attr2', ""),
					content = data.get('content', ""),
				)
		info["status"] = 0
		info["newPage"] = page.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def newStack(request):
	info = dict()

	data = json.loads(request.body)
	try:
		stack = Stack.objects.create(
					owner = request.user.username,
					name = data.get('name', 'Stack ' + str(Stack.objects.filter(owner = request.user.username).count() + 1)),
					priority = data.get('priority', 0),
					attr1 = data.get('attr1', ""),
					attr2 = data.get('attr2', "")
				)
		info["status"] = 0
		info["newStack"] = stack.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def notebook(request, i = 0):
	info = dict()

	try:
		notebook = Notebook.objects.filter(pk = i)[0]

		if request.method == "POST":
			data = json.loads(request.body)
			if 'name' in data:
				notebook.name = data['name']
			if 'stack' in data:
				notebook.stack = data['stack']
			if 'priority' in data:
				if notebook.priority != 0 and data['priority'] !=0:
					notebook.priority = data['priority']
			if 'attr1' in data:
				notebook.attr1 = data['attr1'],
			if 'attr2' in data:
				notebook.attr2 = data['attr2'],
			notebook.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		childPages = Page.objects.filter(notebook = notebook.pk).order_by('-updated')
		info["status"] = 0
		info["notebook"] = model_to_json(notebook)
		info["childPages"] = collection_to_json(childPages)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def notebooks(request):
	info = dict()

	try:
		notebooks = Notebook.objects.filter(owner = request.user.username).order_by('priority', 'name')
		info["status"] = 0
		info["notebooks"] = collection_to_json(notebooks)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def page(request, i = 0):
	info = dict()

	try:
		page = Page.objects.filter(pk = i)[0]

		if request.method == "POST":
			data = json.loads(request.body)
			if 'name' in data:
				page.name = data['name']
			if 'notebook' in data:
				page.notebook = data['notebook']
			if 'priority' in data:
				page.priority = data['priority']
			if 'attr1' in data:
				page.attr1 = data['attr1'],
			if 'attr2' in data:
				page.attr2 = data['attr2'],
			if 'content' in data:
				page.content = data['content']
			page.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		info["status"] = 0
		info["page"] = model_to_json(page)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def stack(request, i = 0):
	info = dict()

	try:
		stack = Stack.objects.filter(pk = i)[0]

		if request.method == "POST":
			data = json.loads(request.body)
			if 'name' in data:
				stack.name = data['name']
			if 'priority' in data:
				stack.priority = data['priority']
			if 'attr1' in data:
				stack.attr1 = data['attr1'],
			if 'attr2' in data:
				stack.attr2 = data['attr2'],
			stack.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		childNotebooks = Notebook.objects.filter(stack = stack.pk).order_by('priority', 'name')
		info["status"] = 0
		info["stack"] = model_to_json(stack)
		info["childNotebooks"] = collection_to_json(childNotebooks)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def stacks(request):
	info = dict()

	try:
		stacks = Stack.objects.filter(owner = request.user.username).order_by('priority', 'name')
		info["status"] = 0
		info["stacks"] = collection_to_json(stacks)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def restorePage(request, i = -1):
	info = dict()

	try:
		page = Page.objects.filter(pk = i)[0]
		page.active = 0
		page.save()
		info["active"] = 0
		info["status"] = 0
		info["restorePage"] = i
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")


@login_required
def trash(request):
	info = dict()

	try:
		pages = Page.objects.filter(owner = request.user.username, active = 1).order_by('-updated')
		info = collection_to_json(pages)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info), content_type="application/json")
