from django.conf.urls import include, url
from django.contrib import admin

from . import views
from .api import MyUserResource

app_name = 'myauth'

urlpatterns = [
        url(r'^$', views.index, name='index'),
#        url(r'register/?$', views.RegisterFormView.as_view(), name='register'),
        url(r'register/?$', views.myregister, name='register'),
        url(r'register/submit/?$', views.myregister_submit, name='register_submit'),
        url(r'login/?$', views.mylogin, name='login'),
        url(r'token/?$', views.get_token, name='token'),
        url(r'login/check/?$', views.mylogin_validate, name='login_validate'),
        url(r'logout/?$', views.mylogout, name='logout'),
        url(r'api/users/', include(MyUserResource.urls())),
        url(r'api/users/$', views.index, name='api'),
        ]
