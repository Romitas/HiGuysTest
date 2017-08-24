from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import MyUser, UserType, MyAuthToken

class MyUserResource(DjangoResource):
    """Restless MyUser resource"""

    preparer = FieldsPreparer(fields={
        'id':'id',
        'username':'user.username',
        'email':'user.email',
        'type':'type.name',
        })

    def is_authenticated(self):
        """API authentication"""

        # Always True (allow all requests) for testing purposes
#        return True 

        # For viewing in browser
        if self.request.user.is_authenticated(): 
            return True

        # For incoming requests
        try:
            token = MyAuthToken.objects.get(token=self.request.META.get('HTTP_AUTHORIZATION','').replace('Token ', ''))
            return True
        except:
            return False

    def list(self):
        """GET /users/"""
        return MyUser.objects.all()

    def detail(self, pk):
        """GET /users/id/"""
        return get_object_or_404(MyUser, pk=pk)

    def create(self):
        """POST /users/"""
        new_user = User.objects.create_user(
                email = self.data['email'],
                username=self.data['email'].split('@')[0],
                password=self.data['password']
                )
        return MyUser.objects.create(
                type=UserType.objects.get(name=self.data['type']),
                user=new_user)

    def update(self, pk):
        """PUT /users/id/"""
        myuser = get_object_or_404(MyUser, pk=pk)

        try:
            myuser.type=UserType.objects.get(name=self.data['type'])
        except KeyError:
            pass
        except UserType.DoesNotExist:
#            return myuser 
            pass # if new type is invalid, skip assigning type, but proceed

        try:
            myuser.user.email = self.data['email']
            myuser.user.username = myuser.user.email.split('@')[0] #TODO: make this a proper method
        except KeyError:
            pass

        try:
            myuser.user.set_password(self.data['password'])
        except KeyError:
            pass

        myuser.save()
        myuser.user.save()

        return myuser

    def delete(self, pk):
        """DELETE /users/id/"""
        MyUser.objects.get(id=pk).user.delete()
