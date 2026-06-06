from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,CreateView,View,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from appss.shop.models import Service,Task
from .models import TaskOffer,ServiceOffer,TaskChat,TaskMessage
from django.urls import reverse_lazy
# Create your views here.

#Task
class ViewsCreateOfferTask(LoginRequiredMixin, CreateView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)  

        task_id = self.kwargs.get('task_id')
        self.task = get_object_or_404(Task, id=task_id)

    model = TaskOffer
    template_name = 'chat/task/offer_create.html'
    fields = ['proposed_price','message']
    success_url =reverse_lazy('shop:home')
    def form_valid(self, form):
        form.instance.product = self.task
        form.instance.executor = self.request.user
        return super().form_valid(form)

class ViewsListOfferTask(LoginRequiredMixin,ListView):
    model = TaskOffer
    template_name = 'chat/task/task_offers_list.html'
    context_object_name = 'offers'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        task_slug = self.kwargs.get('task_slug')
        self.task = get_object_or_404(Task, slug=task_slug)
        

    def get_queryset(self):
        return TaskOffer.objects.filter(product=self.task)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context
#Service
class ViewsCreateOfferService(LoginRequiredMixin,CreateView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)  

        service_id = self.kwargs.get('task_id')
        self.service = get_object_or_404(Service, id=service_id)

    model = ServiceOffer
    template_name = 'chat/service/offer_create.html'
    fields = ['proposed_price','message']
    success_url =reverse_lazy('shop:home')
    def form_valid(self, form):
        form.instance.product = self.service
        form.instance.executor = self.request.user
        return super().form_valid(form)
#Chat
class ViewsCreateChatTask(LoginRequiredMixin,View):
    def post(self, request, task_id):
        # 1. Получаем оффер по id из URL
        offer = get_object_or_404(TaskOffer, id=task_id)

        # 2. Проверяем, что пользователь — владелец задачи
        if request.user != offer.product.user:
            return HttpResponseForbidden("Вы не владелец задачи")

        # 3. Проверяем, что оффер ещё не обработан
        if offer.status != TaskOffer.Status.PENDING:
            return HttpResponseForbidden("Оффер уже принят или отклонён")

        # 4. Меняем статус оффера и сохраняем
        offer.status = TaskOffer.Status.ACCEPTED
        offer.save()

        # 5. Создаём чат и привязываем к офферу
        chat = TaskChat.objects.create(offer=offer,name = offer.product.title)

        # 6. Добавляем участников: заказчика и исполнителя
        chat.members.add(offer.product.user, offer.executor)

        # 7. Перенаправляем на страницу чата (предположим, что у нас есть такой URL)
        return redirect('chat_detail', chat_id=chat.id)
    
class ViewsCreateTaskMessege(LoginRequiredMixin,View):
    def post(self, request, chat_id):
        chat = get_object_or_404(TaskChat,id=chat_id)
        taskmessage = TaskMessage.objects.create(chat=chat,author=request.user.username,content=request.POST.get('content'))
        return redirect('chat_detail', chat_id=chat.id)
    
class ViewsDetailChat(LoginRequiredMixin,DetailView):
    model = TaskChat
    template_name = 'пока в процессе'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['chat_messages'] = self.object.taskmessage_set.all().order_by('timestamp')
        return context

    
    