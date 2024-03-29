from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def userLogin(request):
	info = dict()

	data = json.loads(request.body)
	username = data['username']
	password = data['password']
	
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			info["status"] = 0
			info["msg"] = "login"
		else:
			info["status"] = 1
			info["msg"] = "deactivated"
	else:
		info["status"] = 1
		info["msg"] = "invalid"
	return HttpResponse(json.dumps(info), content_type="application/json")


@csrf_exempt
def userLogout(request):
	info = dict()
	logout(request)
	info["status"] = 0
	info["msg"] = "logout"
	return HttpResponse(json.dumps(info), content_type="application/json")


@csrf_exempt
def userSignUp(request):
	info = dict()
	
	data = json.loads(request.body)
	username = data['username']
	first_name = data['first_name']
	last_name = data.get('last_name', '')
	email = data['email']
	password = data['password']

	if User.objects.filter(username = username):
		info["status"] = 1
		info["msg"] = "alreadyExists"
	else:
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		info["status"] = 0
		info["msg"] = "signUp"
	return HttpResponse(json.dumps(info), content_type="application/json")


@csrf_exempt
@login_required
def userChangePass(request):
	info = dict()
	username = request.user.username
	
	data = json.loads(request.body)
	oldPass = data['oldPassword']
	newPass = data['newPassword']
	user = authenticate(username=username, password=oldPass)
	if user is not None:
		if user.is_active:
			user.set_password(newPass)
			user.save()
			info["status"] = 0
			info["msg"] = "changePass"
		else:
			info["status"] = 1
			info["msg"] = "deactivated"
	else:
		info["status"] = 1
		info["msg"] = "invalid"
	return HttpResponse(json.dumps(info), content_type="application/json")


@csrf_exempt
def userGetInfo(request):
	info = dict()
	if request.user.is_anonymous():
		info["status"] = 0
		info["username"] = "anon"
		info["firstName"] = "Anon"
		info["lastName"] = ""
		info["email"] = ""
		info["role"] = 0
	else:
		info["status"] = 1
		info["username"] = request.user.username
		info["firstName"] = request.user.first_name
		info["lastName"] = request.user.last_name
		info["email"] = request.user.email
		info["role"] = 1
	info["msg"] = "getInfo"
	return HttpResponse(json.dumps(info), content_type="application/json")


@csrf_exempt
@login_required
def userSetInfo(request):
	info = dict()

	data = json.loads(request.body)
	request.user.first_name = data.get('firstName', request.user.first_name)
	request.user.last_name = data.get('lastName', request.user.last_name)
	
	request.user.save()
	info["status"] = 0
	info["msg"] = "setInfo"
	return HttpResponse(json.dumps(info), content_type="application/json")