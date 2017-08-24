# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser
from jwt import encode, decode

class UserType(models.Model):
    """UserType model: store possible user type values"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MyUser(models.Model):
    """Basic User model extension, doing nothing but adding a UserType field"""
    user = models.OneToOneField(User, default=None, blank=True, null=True)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.user.username, str(self.type))

class MyAuthToken(models.Model):
    """Костыли и Велосипеды Inc."""

    user = models.OneToOneField(User)
    token = models.CharField(max_length=300, default='')

    def generate_token(self):
        data = {'email':self.user.email, 'type':str(self.user.myuser.type)}
        secret = settings.SECRET_KEY
        return encode(data, secret, algorithm='HS256')

    def save(self, *args, **kwargs):
        self.token = self.generate_token()
        super(MyAuthToken, self).save(*args, **kwargs)

    def __str__(self):
        return self.token
