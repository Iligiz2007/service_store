from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect

from appss.user.tasks import send_verification_email
from .forms import FormRegisterUser,FormLoginUser
from django.urls  import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView,DetailView, TemplateView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .models import User,Profile
from django.shortcuts import get_object_or_404
from django.views import View 
from django.contrib import messages


class ViewsRegisterUser(UserPassesTestMixin ,CreateView):
    template_name = 'user/register.html'
    form_class = FormRegisterUser
    success_url = reverse_lazy('shop:home')
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
        return  redirect(reverse_lazy('shop:home'))
    
class ViewsLoginUser(UserPassesTestMixin,LoginView):
    template_name = 'user/login.html'
    form_class = FormLoginUser
    success_url = reverse_lazy('shop:home')
    redirect_authenticated_user = True


    def test_func(self) -> bool | None:
 
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return  redirect(reverse_lazy('shop:home'))

class ViewsLogout(UserPassesTestMixin,LogoutView):
    template_name = 'user/logout.html'         
    next_page = reverse_lazy('shop:home')       
    http_method_names = ['get','post']

    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return  redirect(reverse_lazy('shop:home'))
    
class ViewsDetailProfileMy(LoginRequiredMixin,DetailView):
    template_name = 'user/detail_myuser.html'
    model = Profile
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile
    
class ViewsDetailProfile(LoginRequiredMixin, DetailView):
    template_name = 'user/detail_user.html'
    model = Profile
    context_object_name = 'profile'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ViewsUpdateProfile(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['bio','birth_date','avatar','is_verified']
    template_name = 'user/update_profale.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('detail_user_my')


    def get_object(self):
        return self.request.user.profile

class GuestMenuView(TemplateView):
    def get(self, request,*args, **kwargs):
        return render(request,'templates_htmx/menu_not_in.html')

    
class ViewsChangestatusSalesman(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.status = True
        profile.save()
        return render(request, 'templates_htmx/menu_user_seller.html')


class ViewsChangestatusBuyer(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.status = False
        profile.save()
        return render(request, 'templates_htmx/menu_user_buyer.html')

class ViewsGetMenu(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        if profile.status:
            return render(request, 'templates_htmx/menu_user_seller.html')
        else:
            return render(request, 'templates_htmx/menu_user_buyer.html')
        
# Активация user
class ViewsActiveUser(View):
    def get(self, request,*args, **kwargs):
        uuid = self.kwargs['uuid']
        user = get_object_or_404(User,verification_uuid=uuid)
        profile = user.profile
        if not profile.is_verified:
            profile.is_verified = True
            profile.save()
            messages.success(request, 'Ваш аккаунт подтверждён!')
        return redirect('login')

class ViewsMail(View):
    def post(self, request,*args, **kwargs):
        user = request.user
        profile = user.profile
        if not profile.is_verified:
            send_verification_email.delay(user.id)
            messages.success(request, 'Письмо с подтверждением отправлено! Проверьте почту.')
        else:
            messages.info(request, 'Ваш аккаунт уже активирован.')
        return redirect('detail_user_my')
            

