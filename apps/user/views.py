from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import FormRegisterUser,FormLoginUser
from django.urls  import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView,DetailView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .models import User
from django.shortcuts import get_object_or_404
# Create your views here.

class ViewsRegisterUser(UserPassesTestMixin ,CreateView):
    template_name = 'user/register.html'
    form_class = FormRegisterUser
    success_url = reverse_lazy('home')
    redirect_authenticated_user  = False
    def form_valid(self, form):
        service = form.save()
        if 'avatar' in self.request.FILES:
            service.avatar = self.request.FILES['avatar']
            service.save()
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
 
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return  redirect(reverse_lazy('home'))
    
class ViewsLoginUser(UserPassesTestMixin,LoginView):
    template_name = 'user/login.html'
    form_class = FormLoginUser
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True


    def test_func(self) -> bool | None:
 
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return  redirect(reverse_lazy('home'))

class ViewsLogout(UserPassesTestMixin,LogoutView):
    template_name = 'user/logout.html'         
    next_page = reverse_lazy('home')       
    http_method_names = ['get','post']

    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return  redirect(reverse_lazy('home'))

class ViewsDetailUser(LoginRequiredMixin, TemplateView):
    template_name = 'user/detail_user.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_obj'] = self.request.user
        return context