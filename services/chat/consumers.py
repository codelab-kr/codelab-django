import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        # 그룹 참여
        await self.channel_layer.group_add(  # type: ignore
            self.room_group_name,
            self.channel_name,
        )
        # 연결 수락
        await self.accept()

    async def disconnect(self, close_code):
        # 그룹 탈퇴
        await self.channel_layer.group_discard(  # type: ignore
            self.room_group_name,
            self.channel_name,
        )

    # 웹소켓에서 메시지 수신
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # 그룹에 메시지 전송
        await self.channel_layer.group_send(  # type: ignore
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': timezone.now().isoformat(),  # iso 8601
            },
        )

    # 그룹에서 메시지 수신
    async def chat_message(self, event):
        # 웹소켓으로 메시지 전송
        await self.send(text_data=json.dumps(event))
