from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from notes.models import *
import json
from datetime import datetime
# Create your views here.

@csrf_exempt
@login_required
def home(request):
	info = dict()

	return HttpResponse(json.dumps(info))


@csrf_exempt
@login_required
def newBoard(request):
	info = dict()
	board = Board.objects.create(
				owner = request.user.username,
				name = request.POST.get('name', str(datetime.now())),
				parent = request.POST.get('parent', Board.objects.filter(owner = request.user.username, parent = 0)[0].pk),
				priority = request.POST.get('priority', 0),
				attr1 = request.POST.get('attr1', ""),
				attr2 = request.POST.get('attr2', "")
			)
	board.save()
	info["status"] = 0
	info["newBoard"] = board.pk
	return HttpResponse(json.dumps(info))


@csrf_exempt
@login_required
def newNote(request):
	info = dict()
	if 'board' not in request.POST:
		board = Board.objects.filter(owner = request.user.username, parent = 0)[0]
	else:
		board = Board.objects.filter(pk = request.POST.get('board'))[0]
	note = Note.objects.create(
				owner = request.user.username,
				name = request.POST.get('name', str(datetime.now())),
				board = board,
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


@csrf_exempt
@login_required
def delBoard(request,  i = -1):
	info = dict()
	board = Board.objects.filter(pk = i)[0]
	if board.parent == 0:
		info["status"] = 1
		info["delBoard"] = i
		info["msg"] = "rootBoard"
	else:
		notes = Note.objects.filter(board = i)
		for note in notes:
			note.board = Board.objects.filter(pk = board.parent)[0]
			note.save()
		board.delete()
		info["status"] = 0
		info["delBoard"] = i
	return HttpResponse(json.dumps(info))


@csrf_exempt
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


@csrf_exempt
@login_required
def board(request, i = 0):
	info = dict()

	return HttpResponse(json.dumps(info))


@csrf_exempt
@login_required
def note(request, i = 0):
	info = dict()

	return HttpResponse(json.dumps(info))