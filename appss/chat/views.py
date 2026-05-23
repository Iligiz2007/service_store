from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from appss.shop.models import Service
# Create your views here.


"""class ViewsOffers(LoginRequiredMixin,CreateView):
    model = Offer
    template_name = 'chat/offer_create.html'
    context_object_name = 'offer'
    def dispatch(self, request, *args, **kwargs):
        self.service = get_object_or_404(Service,id=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.service = self.service
        form.instance.executor = self.request.user
        return super().form_valid(form)
    
# нужно дописать шаблон 
'''class ViewsChat(LoginRequiredMixin,ListView):
    model = Chat
    template_name =''
    context_object_name ='chat'

    def get_queryset(self):
        return Chat.objects.filter(participants=self.request.user) '''   
"""