# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def secret(request):
    """Special 'Login Required' Page for testing matters"""
    return HttpResponse('\
            <p>Welcome to our Official Top Secret Page, %s!</p>\
            <a href="/">Back</a>' % request.user.username)

def index(request):
    user = 'guest'
    if request.user.is_authenticated():
        user = request.user.email
    return render(request, 'index.html', {'user': user})
