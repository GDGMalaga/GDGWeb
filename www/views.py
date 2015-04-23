from django.shortcuts import render

from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login


def home(request):
	"""
	Displays the homepage.
	"""
	return render(request, 'home.html')

def calendario(request):
    '''
    Displays the calendar
    '''
    return render(request, "calendario.html")

def grupos(request):
    '''
    Displays the groups
    '''
    return render(request, "grupos.html")

def accede(request):
    '''
    Displays the access
    '''
    return render(request,"accede.html")

def login(request):
    '''
    To authenticate a given username and password, use authenticate().
    It takes credentials in the form of keyword arguments, 
    for the default configuration this is username and password, 
    and it returns a User object if the password is valid for the given username. 
    If the password is invalid, authenticate() returns None.
    '''
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')

    return render(request, 'home.html')
    