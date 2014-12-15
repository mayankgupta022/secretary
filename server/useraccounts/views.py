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

	username = request.POST['username']
	password = request.POST['password']
	
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
	return HttpResponse(json.dumps(info))


@csrf_exempt
def userLogout(request):
	info = dict()
	logout(request)
	info["status"] = 0
	info["msg"] = "logout"
	return HttpResponse(json.dumps(info))


@csrf_exempt
def userSignUp(request):
	info = dict()
	
	username = request.POST['username']
	first_name = request.POST['first_name']
	last_name = request.POST.get('last_name', '')
	email = request.POST['email']
	password = request.POST['password']

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
	return HttpResponse(json.dumps(info))


@csrf_exempt
@login_required
def userChangePass(request):
	info = dict()
	username = request.user.username
	
	oldPass = request.POST['oldPass']
	newPass = request.POST['newPass']
	confirmPass = request.POST['confirmPass']
	
	if newPass != confirmPass:
		info["status"] = 1
		info["msg"] = "mismatch"
	else:
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
	return HttpResponse(json.dumps(info))


@csrf_exempt
def userGetInfo(request):
	info = dict()
	if request.user.is_anonymous():
		info["status"] = 0
		info["msg"] = "getInfo"
		info["username"] = "anon"
		info["first_name"] = "Anon"
		info["last_name"] = ""
		info["email"] = ""
	else:
		info["status"] = 1
		info["msg"] = "getInfo"
		info["username"] = request.user.username
		info["first_name"] = request.user.first_name
		info["last_name"] = request.user.last_name
		info["email"] = request.user.email
	return HttpResponse(json.dumps(info))


@csrf_exempt
@login_required
def userSetInfo(request):
	info = dict()

	request.user.first_name = request.POST.get('first_name', request.user.first_name)
	request.user.last_name = request.POST.get('last_name', request.user.last_name)
	
	request.user.save()
	info["status"] = 0
	info["msg"] = "setInfo"
	return HttpResponse(json.dumps(info))