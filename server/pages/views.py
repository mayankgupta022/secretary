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
		info["status"] = 0
		info["pages"] = collection_to_json(pages)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


@login_required
def newNotebook(request):
	info = dict()

	try:
		notebooks = Notebook.objects.filter(owner = request.user.username)
		if not notebooks:
			name = "Default Notebook"
			priority = 0
		else:
			name = request.POST.get('name', 'Notebook ' + str(Notebook.objects.filter(owner = request.user.username).count() + 1))
			priority = request.POST.get('priority', 1)

		notebook = Notebook.objects.create(
					owner = request.user.username,
					name = name,
					stack = request.POST.get('stack', 0),
					priority = priority,
					attr1 = request.POST.get('attr1', ""),
					attr2 = request.POST.get('attr2', "")
				)
		info["status"] = 0
		info["newNotebook"] = notebook.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def newPage(request):
	info = dict()

	try:
		if 'notebook' in request.POST:
			notebook = Notebook.objects.filter(owner = request.user.username, notebook = request.POST['notebook'])[0]
		else:
			notebook = Notebook.objects.filter(owner = request.user.username, priority = 0)[0]
		page = Page.objects.create(
					owner = request.user.username,
					name = request.POST.get('name', 'Untitled ' + str(Page.objects.filter(owner = request.user.username).count() + 1)),
					notebook = notebook,
					context = request.POST.get('context', 0),
					active = request.POST.get('active', 0),
					priority = request.POST.get('priority', 0),
					attr1 = request.POST.get('attr1', ""),
					attr2 = request.POST.get('attr2', ""),
					content = request.POST.get('content', ""),
				)
		info["status"] = 0
		info["newPage"] = page.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def newStack(request):
	info = dict()

	try:
		stack = Stack.objects.create(
					owner = request.user.username,
					name = request.POST.get('name', 'Stack ' + str(Stack.objects.filter(owner = request.user.username).count() + 1)),
					priority = request.POST.get('priority', 0),
					attr1 = request.POST.get('attr1', ""),
					attr2 = request.POST.get('attr2', "")
				)
		info["status"] = 0
		info["newStack"] = stack.pk
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def notebook(request, i = 0):
	info = dict()

	try:
		notebook = Notebook.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in request.POST:
				notebook.name = request.POST['name']
			if 'stack' in request.POST:
				notebook.stack = request.POST['stack']
			if 'priority' in request.POST:
				if notebook.priority != 0 and request.POST['priority'] !=0:
					notebook.priority = request.POST['priority']
			if 'attr1' in request.POST:
				notebook.attr1 = request.POST['attr1'],
			if 'attr2' in request.POST:
				notebook.attr2 = request.POST['attr2'],
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

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


@login_required
def page(request, i = 0):
	info = dict()

	try:
		page = Page.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in request.POST:
				page.name = request.POST['name']
			if 'notebook' in request.POST:
				page.notebook = request.POST['notebook']
			if 'priority' in request.POST:
				page.priority = request.POST['priority']
			if 'attr1' in request.POST:
				page.attr1 = request.POST['attr1'],
			if 'attr2' in request.POST:
				page.attr2 = request.POST['attr2'],
			if 'content' in request.POST:
				page.content = request.POST['content']
			page.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		info["status"] = 0
		info["page"] = model_to_json(page)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


@login_required
def stack(request, i = 0):
	info = dict()

	try:
		stack = Stack.objects.filter(pk = i)[0]

		if request.method == "POST":
			if 'name' in request.POST:
				stack.name = request.POST['name']
			if 'priority' in request.POST:
				stack.priority = request.POST['priority']
			if 'attr1' in request.POST:
				stack.attr1 = request.POST['attr1'],
			if 'attr2' in request.POST:
				stack.attr2 = request.POST['attr2'],
			stack.save();
			info["msg"] = "CHANGED"
		else:
			info["msg"] = "NOCHANGE"

		childNotebooks = Notebook.objects.filter(stack = stack.pk).order_by('priority', 'name')
		info["status"] = 0
		info["stack"] = model_to_json(stack)
		info["childNotebooks"] = collection_to_json(childPages)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


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

	return HttpResponse(json.dumps(info))


@login_required
def trash(request):
	info = dict()

	try:
		pages = Page.objects.filter(owner = request.user.username, active = 1).order_by('-updated')
		info["status"] = 0
		info["pages"] = collection_to_json(pages)
	except Exception as e:
		info["status"] = 1
		info["msg"] = e.message + str(type(e))

	return HttpResponse(json.dumps(info))
