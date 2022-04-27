from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Attendance, Worker,Site
from django.views.generic.edit import CreateView

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

class Attendform(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(Attendform, self).__init__(*args, **kwargs)
        self.fields['Worker']=forms.ModelChoiceField(
            queryset=Worker.objects.filter(owner=user))
        
