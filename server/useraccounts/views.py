from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
	
	user = User.objects.create_user(username, email, password)
	user.first_name = first_name
	user.last_name = last_name
	user.save()
	info["status"] = 0
	info["msg"] = "signUp"
	return HttpResponse(json.dumps(info))


@csrf_exempt
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