from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def chatbot_index(request):
    return render(request, "chat/chatgpt_index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
