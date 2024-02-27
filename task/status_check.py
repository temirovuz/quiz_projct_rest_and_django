import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class StatusCheckConsumer(JsonWebsocketConsumer):

    def connect(self):
        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            'check_status',
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'check_status',
            self.channel_name,
        )

    def receive(self, connect, **kwargs):
        print('receive')

    def get_status(self, event):
        self.send_json(event['data'])
