# <!-----  sync code -->>
# import json
#
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
#
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event["message"]
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))


# ! ---- async code --->
import json

import openai
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))


openai.api_key = settings.OPENAI_API_KEY


class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_message = text_data_json['message']

        # Generate the response using OpenAI's API
        response = await self.chatbot_response(user_message)

        # Send the OpenAI generated message back to WebSocket
        await self.send(text_data=json.dumps({
            'message': response
        }))

    async def chatbot_response(self, message):
        # Call OpenAI's API to generate a response
        try:
            openai_response = openai.chat.completions.create(

                # engine="davinci",  # or specify another model
                # prompt=message,
                # max_tokens=150\

                messages=[
                    {
                        "role": "user",
                        "content": message,
                    }
                ],
                # model="gpt-3.5-turbo",
                model="gpt-3.5-turbo"

            )
            return openai_response.choices[0].text.strip()
        # except openai.OpenAIError as e:
        #     # Handle API errors here
        #     return f"An error occurred: {str(e)}"
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
