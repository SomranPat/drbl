from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Worker,Site

class CreateEmpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class workForm(ModelForm):
    class Meta:
        model = Worker
        fields ='__all__'


class siteform(ModelForm):
    class Meta:
        model = Site
        fields = '__all__'
        
