from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/task/<int:chat_id>/', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/service/<int:chat_id>/', consumers.ChatConsumer.as_asgi()),
]