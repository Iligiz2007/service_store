from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView
from .forms import FormService
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service
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
    