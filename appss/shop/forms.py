from django import forms
from django.forms import ModelForm
from .models import Service,Task

class FormService(ModelForm):
    
    class Meta:
        model = Service
        fields = ("title","description","price")


class FormTask(ModelForm):
    class Meta:
        model = Task
        fields = ("title","description","price")