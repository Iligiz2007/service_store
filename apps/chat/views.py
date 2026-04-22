from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat
# Create your views here.


class ViewsOffers():
    pass 
# нужно дописать шаблон 
'''class ViewsChat(LoginRequiredMixin,ListView):
    model = Chat
    template_name =''
    context_object_name ='chat'

    def get_queryset(self):
        return Chat.objects.filter(participants=self.request.user) '''   
