import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # 연결 수락
        self.accept()

    def disconnect(self, close_code):
        pass

    # 웹소켓에서 메시지 수신
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 웹소켓으로 메시지 전송
        self.send(text_data=json.dumps({'message': message}))
