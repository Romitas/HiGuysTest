# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .models import MyUser, UserType

def index(request):
    """Index page, redirect to API view"""
    return HttpResponseRedirect(reverse('myauth:api'))

def mylogin(request):
    """Login form page"""
    try:
        return render(request, 'myauth/login.html', {'redirect_url': request.GET['next']})
    except:
        return render(request, 'myauth/login.html', {'redirect_url': '/'})

def mylogout(request):
    """Log out, redirect to index"""
    logout (request)
    return HttpResponseRedirect('/')

@csrf_exempt
def get_token(request):
    email = request.POST['email']
    password = request.POST['password']
    username = email.split('@')[0] 

    user = authenticate(request, username=username, password=password)
    if user is not None: 
        data = {'token': str(user.myauthtoken)}
        return JsonResponse(data)
    else:
        return HttpResponse('')


def mylogin_validate(request):
    """Validate login credentials"""

    email = request.POST['email']
    password = request.POST['password']
    username = email.split('@')[0] 

    user = authenticate(request, username=username, password=password)
    if user is not None: 
        login(request, user)

        try:
            return HttpResponseRedirect(request.GET['next'])
        except:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'myauth/login.html', {
            'redirect_url': request.GET['next'],
            'error_message': 'Invalid login credentials. Please try again.'
            })

def myregister(request):
    """New user register form page"""
    return render(request, 'myauth/register.html', {
        'types': UserType.objects.all()
        })

def myregister_submit(request):
    """New user registration"""

    # Input validating
    try:
        email = request.POST['email']
        if not '@' in email: # if email is obviously not valid
            raise Exception()

        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation: # if passwords do not match
            raise Exception()

        type = UserType.objects.get(name=request.POST['type'])

        username = email.split('@')[0] # username is generated automatically
        if User.objects.filter(username=username): # if user with such username already exists
            raise Exception()
    except:
        return render(request, 'myauth/register.html', {
            'types': UserType.objects.all(),
            'error_message': 'Invalid credentials. Please try again.'
            })

    # Creating new user, adding MyUser extension and creating an API token
    user = User.objects.create_user(username=username, email=email, password=password)
    my_user = MyUser.objects.create(type=type, user=user)
    MyAuthToken.objects.create(user=user)

    return HttpResponseRedirect(reverse('myauth:login'))
