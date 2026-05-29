from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from appss.shop.models import Service,Task
from .models import TaskOffer
from django.urls import reverse_lazy
# Create your views here.


class ViewsCreateOffer(LoginRequiredMixin, CreateView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)  

        task_id = self.kwargs.get('task_id')
        self.task = get_object_or_404(Task, id=task_id)

    model = TaskOffer
    template_name = 'chat/offer_create.html'
    fields = ['proposed_price','message']
    success_url =reverse_lazy('shop:home')
    def form_valid(self, form):
        form.instance.product = self.task
        form.instance.executor = self.request.user
        return super().form_valid(form)
    
    

    """
# нужно дописать шаблон 
'''class ViewsChat(LoginRequiredMixin,ListView):
    model = Chat
    template_name =''
    context_object_name ='chat'

    def get_queryset(self):
        return Chat.objects.filter(participants=self.request.user) '''   
"""