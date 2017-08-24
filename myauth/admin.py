# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from .models import MyUser, UserType

# Register your models here.

class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False

class MyUserAdmin(UserAdmin):
    list_display = ('email',  'myuser')
    inlines = (MyUserInline, )

admin.site.unregister(Group) # won't need groups management

admin.site.unregister(User) 
admin.site.register(User, MyUserAdmin)
admin.site.register(UserType, admin.ModelAdmin)
