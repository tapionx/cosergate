from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
	if request.user.is_authenticated():
		return redirect('/home')
	else:
		return render(request, 'web/main.html', {})

def cosergate_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('/home') 
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
	
@login_required(login_url='/')
def home(request):
	return render(request, 'web/home.html', {})

@login_required(login_url='/')	
def account(request):
	user = request.user
	return render(request, 'web/account.html', {user: user})




















	

