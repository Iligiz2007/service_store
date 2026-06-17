import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        # Определяем тип чата по пути запроса
        path = self.scope['path']
        if '/ws/chat/task/' in path:
            self.chat_type = 'task'
        else:
            self.chat_type = 'service'
        
        self.room_group_name = f'{self.chat_type}_chat_{self.chat_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'author': event['author'],
            'content': event['content'],
            'timestamp': event['timestamp'],
        }))