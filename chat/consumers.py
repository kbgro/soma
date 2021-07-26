import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """accept connection"""
        self.accept()

    def disconnect(self, code):
        """Disconnect websocket"""

    def receive(self, text_data=None, bytes_data=None):
        """Receives message from websocket."""
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({"message": message}))
