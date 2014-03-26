from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
	if request.user.is_authenticated():
		return HttpResponse('you have already logged in')
	else:
		return render(request, 'web/index.html', {})

def cosergate_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse('login_succeed')
		else:
			return HttpResponse('disabled user')
	else:
		return HttpResponse('login_failed')

def cosergate_logout(request):
	logout(request)
	return redirect('/')

def cosergate_signup(request):
	username = request.POST['username']
	password = request.POST['password']
	name = request.POST['name']
	surname = request.POST['surname']	
	email = request.POST['email']
	user = User.objects.create_user(username, email, password)
	user.first_name = name
	user.last_name = surname
	user.save()
	return HttpResponse('user created')
