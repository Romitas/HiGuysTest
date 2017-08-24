# -*- coding: utf-8 -*-

"""higuystest URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^secret/', views.secret, name='secret'),
    url(r'^account/', include('myauth.urls')),
    url(r'^admin/?', admin.site.urls),
    url(r'^admin/?$', views.index, name='admin'),
]
