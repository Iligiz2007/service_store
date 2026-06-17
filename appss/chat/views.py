from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,CreateView,View,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from appss.shop.models import Service,Task
from .models import TaskOffer,ServiceOffer,TaskChat,TaskMessage,ServiceChat,ServiceMessage
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
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
    template_name = 'chat/service/offers_create.html'
    fields = ['proposed_price','message']
    success_url =reverse_lazy('shop:home')
    def form_valid(self, form):
        form.instance.product = self.service
        form.instance.executor = self.request.user
        return super().form_valid(form)

class ViewsListOfferService(LoginRequiredMixin,ListView):
    model = ServiceOffer
    template_name = 'chat/service/service_offers_list.html'
    context_object_name = 'service_offers'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        service_slug = self.kwargs.get('service_slug')
        self.service = get_object_or_404(Service, slug=service_slug)
        

    def get_queryset(self):
        return ServiceOffer.objects.filter(product=self.service)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.service
        return context
    

class ViewsCreateChatService(LoginRequiredMixin,View):
    def post(self, request, service_id):
        offer = get_object_or_404(ServiceOffer, id=service_id)
        offers_to_reject = ServiceOffer.objects.filter(
        product=offer.product,
            status=ServiceOffer.Status.PENDING
        ).exclude(id=service_id)

        if request.user != offer.product.user:
            return HttpResponseForbidden("Вы не владелец задачи")
        if offer.status != ServiceOffer.Status.PENDING:
            return ServiceOffer("Оффер уже принят или отклонён")
        offer.status = ServiceOffer.Status.ACCEPTED
        offers_to_reject.update(status=ServiceOffer.Status.REJECTED)
        offer.save()

        chat = ServiceChat.objects.create(offer=offer,name = offer.product.title)

        chat.members.add(offer.product.user, offer.executor)

        return redirect('service_chat_detail', chat_id=chat.id)

class ViewsDetailChatService(LoginRequiredMixin, DetailView):
    model = ServiceChat
    context_object_name = 'chat'
    template_name = 'chat/task/list_message_task.html'  # Всегда фрагмент
    pk_url_kwarg = 'chat_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_post_url'] = 'create_message_service'
        context['chat_messages'] = self.object.servicemessage_set.all().order_by('timestamp')
        context['chat_type'] = 'service'   # <-- добавить
        return context
    
class ViewsCreateServiceMessege(LoginRequiredMixin, View):
    def post(self, request, chat_id):
        chat = get_object_or_404(ServiceChat, id=chat_id)
        content = request.POST.get('content', '').strip()
        if content:
            msg = ServiceMessage.objects.create(chat=chat, author=request.user, content=content)
            # Отправляем уведомление в группу WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'service_chat_{chat.id}',
                {
                    'type': 'chat_message',   # вызывает метод chat_message в Consumer
                    'author': request.user.username,
                    'content': content,
                    'timestamp': msg.timestamp.strftime('%H:%M'),
                }
            )
        # Дальше твой обычный возврат HTML через HTMX (render_to_string и HttpResponse)
        messages = chat.servicemessage_set.all().order_by('timestamp')
        html = render_to_string('chat/task/list_message_task.html', {  # или как у тебя называется этот файл
            'chat': chat,
            'chat_messages': messages,
        })
        return HttpResponse(html)
class ViewsListChatService(LoginRequiredMixin,ListView):
    model = ServiceChat
    context_object_name = 'chat_list'
    template_name = 'chat/task/list_chat.html'
    def get_queryset(self):
        return ServiceChat.objects.filter(members=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_chat'] = 'service_chat_detail'
        context['message_post_url'] = 'create_message_service'
        chats_with_interlocutor = []
        for chat in context['chat_list']:
            interlocutor = chat.members.exclude(id=self.request.user.id).first()
            chats_with_interlocutor.append({
                'chat': chat,
                'interlocutor': interlocutor
            })
        context['chats_with_interlocutor'] = chats_with_interlocutor
        return context

#Chat
class ViewsCreateChatTask(LoginRequiredMixin,View):
    def post(self, request, offer_id):
        offer = get_object_or_404(TaskOffer, id=offer_id)
        offers_to_reject = TaskOffer.objects.filter(
        product=offer.product,
            status=TaskOffer.Status.PENDING
        ).exclude(id=offer_id)

        if request.user != offer.product.user:
            return HttpResponseForbidden("Вы не владелец задачи")
        if offer.status != TaskOffer.Status.PENDING:
            return HttpResponseForbidden("Оффер уже принят или отклонён")
        offer.status = TaskOffer.Status.ACCEPTED
        offers_to_reject.update(status=TaskOffer.Status.REJECTED)
        offer.save()

        chat = TaskChat.objects.create(offer=offer,name = offer.product.title)

        chat.members.add(offer.product.user, offer.executor)

        return redirect('task_chat_detail', chat_id=chat.id)
    
class ViewsCreateTaskMessege(LoginRequiredMixin, View):
    def post(self, request, chat_id):
        chat = get_object_or_404(TaskChat, id=chat_id)
        content = request.POST.get('content', '').strip()
        if content:
            msg = TaskMessage.objects.create(chat=chat, author=request.user, content=content)
            # Отправляем уведомление в группу WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'task_chat_{chat.id}',
                {
                    'type': 'chat_message',   # вызывает метод chat_message в Consumer
                    'author': request.user.username,
                    'content': content,
                    'timestamp': msg.timestamp.strftime('%H:%M'),
                }
            )
        # Дальше твой обычный возврат HTML через HTMX (render_to_string и HttpResponse)
        messages = chat.taskmessage_set.all().order_by('timestamp')
        html = render_to_string('chat/task/list_message_task.html', {  # или как у тебя называется этот файл
            'chat': chat,
            'chat_messages': messages,
        })
        return HttpResponse(html)


class ViewsDetailChatTask(LoginRequiredMixin, DetailView):
    model = TaskChat
    context_object_name = 'chat'
    template_name = 'chat/task/list_message_task.html'  # Всегда фрагмент
    pk_url_kwarg = 'chat_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_post_url'] = 'create_message_task'
        context['chat_messages'] = self.object.taskmessage_set.all().order_by('timestamp')
        context['chat_type'] = 'task'   # <-- добавить
        return context


class ViewsListChatTask(LoginRequiredMixin,ListView):
    model = TaskChat
    context_object_name = 'chat_list'
    template_name = 'chat/task/list_chat.html'
    def get_queryset(self):
        return TaskChat.objects.filter(members=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_chat'] = 'task_chat_detail'
        chats_with_interlocutor = []
        for chat in context['chat_list']:
            interlocutor = chat.members.exclude(id=self.request.user.id).first()
            chats_with_interlocutor.append({
                'chat': chat,
                'interlocutor': interlocutor
            })
        context['chats_with_interlocutor'] = chats_with_interlocutor
        return context

    
    
    
    