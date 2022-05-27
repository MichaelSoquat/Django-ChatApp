from datetime import date, datetime
from datetime import date
from telnetlib import LOGOUT
from django.dispatch import receiver
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
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
    if request.method == 'POST':
        print("Received data" + request.POST['textmessage'])
        try:
            myChat = Chat.objects.get(id=1)
        except:
            myChat = Chat.objects.create(id=1)
            myChat.save()
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        print(new_message)
        serialized_obj = serializers.serialize('json', [new_message,])
        print(serialized_obj)
        return JsonResponse(serialized_obj[1:-1], safe=False)
    date_joined=request.user.date_joined
    chatMessages = Message.objects.filter(time_created_at__gte=date_joined)
    return render(request, 'chat/index.html', {'messages': chatMessages})

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

