from django.urls import re_path

from . import consumers

websocket_urlpatterns = [

    # as_asgi classmethod in order to get an ASGI application that will instantiate an instance of our
    # consumer for each user-connection. same as as_view()

    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chatbot/$', consumers.ChatBotConsumer.as_asgi()),
]
