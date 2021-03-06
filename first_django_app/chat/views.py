from datetime import date, datetime
from datetime import date
from telnetlib import LOGOUT
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Chat, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.db import models
# login is required


def redirect(request):
    return HttpResponseRedirect('/chat/')
@login_required(login_url='/login/')
#render chat content, create message object
def index(request):
    if request.method == 'POST' and 'chat' in request.POST:
        newChat = Chat.objects.create(name = request.POST['chat'])
        newChat.save()
        serialized_obj = serializers.serialize('json', [newChat,])
        return JsonResponse(serialized_obj[1:-1], safe=False,)
   
    if request.method == 'GET':
        if len(Chat.objects.all()) > 0:
            date_joined=request.user.date_joined
            chatMessages = Message.objects.filter(time_created_at__gte=date_joined)
            chats = Chat.objects.all()
            return render(request, 'chat/index.html', {'chats': chats, 'noChatSelected': True})
        else:
            return render(request, 'chat/index.html', {'noChat': True,})

def channel(request, name):
    if request.method == 'POST' and 'textmessage' in request.POST:
        print("Received data" + request.POST['textmessage'])
        print(name)
        try:
            myChat = Chat.objects.get(name=name)
        except:
            myChat = Chat.objects.create(id = 1, name = 1)
            myChat.save()
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        print(new_message)
        serialized_obj = serializers.serialize('json', [new_message,])
        print(serialized_obj)
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chats = Chat.objects.all()
    chatMessages = Message.objects.filter(chat__name = name)
    print(chatMessages)
    return render(request, 'chat/index.html', {'messages': chatMessages, 'chats': chats})



#login
def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password= request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request,'auth/login.html', {'redirect': redirect})



#register
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            user.date_joined = models.DateTimeField(default=datetime.now())
            username = form.cleaned_data.get('username')
            login(request, user)
            return HttpResponseRedirect('/chat/')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "auth/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "auth/register.html",
                  context={"form":form})



#logout
def logout_view(request):
    logout(request) 
    return HttpResponseRedirect('/login/')

