from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

def index(request):
    return render(request,"posts/frame.html.dj")

def profile(request, username):
    return render(request, "posts/frame.html.dj",{'user':username})

def activity(request, username=None):
    return render(request, "posts/frame.html.dj", {'user':username})

