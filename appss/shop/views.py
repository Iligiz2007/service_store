from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,ListView,DetailView
from .forms import FormService
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service
# Create your views here.

class ViewsService(LoginRequiredMixin,CreateView):
    model = Service
    template_name = "shop/service_form.html"
    form_class = FormService
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        service = form.save()
        return super().form_valid(form)


class ViewsIndex(TemplateView):
    template_name = 'index.html'

class ViewsDetialService(DetailView):
    model = Service
    template_name = 'shop/detail_service.html'
    context_object_name = "service"


class ViewsListService(ListView):
    model = Service
    template_name = "shop/list_service.html"
    context_object_name = "service"
    