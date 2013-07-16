from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"posts/frame.html.dj")
