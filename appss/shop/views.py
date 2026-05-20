from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView
from .forms import FormService,FormTask
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service,Task
# Create your views here.

class ViewsService(LoginRequiredMixin,CreateView):
    model = Service
    template_name = "shop/service_form.html"
    form_class = FormService
    success_url = reverse_lazy('shop:home')
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

class ViewsUserListService(ListView):
    model = Service
    template_name = 'shop/list_service_my.html'
    context_object_name = "service"
    def get_queryset(self):
        return Service.objects.filter(user=self.request.user)

class ViewsUpdateService(UpdateView,LoginRequiredMixin):
    model = Service
    fields = ['title','description','price']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'shop/service_update_form.html'
    success_url = reverse_lazy('shop:list_service_my')
    context_object_name = 'service'

#Task

class ViewsFormTask(LoginRequiredMixin,CreateView):
    model = Task
    form_class = FormTask
    template_name = 'shop/task/form_create_task.html'
    success_url = reverse_lazy('shop:home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ViewsDetailTask(DetailView):
    model = Task
    template_name = 'shop/task/detail_task.html'
    context_object_name = 'task'

class ViewsListTaskMy(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'shop/task/list_task_my.html'
    context_object_name = 'task'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class ViewsListTask(ListView):
    model = Task
    template_name = 'shop/task/list_task.html'
    context_object_name = 'task'
    def get_queryset(self):
        return Task.objects.all()

class ViewsUpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','price']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'shop/task/update_task.html'
    success_url = reverse_lazy('shop:list_task_my')