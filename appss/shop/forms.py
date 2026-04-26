from django import forms
from django.forms import ModelForm
from .models import Service

class FormService(ModelForm):
    
    class Meta:
        model = Service
        fields = ("title","description","price")
