from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from posts.models import UserProfile, Post

def index(request):
    return render(request,"posts/frame.html.dj")

def profile(request, username):
    try: 
        user = User.objects.get(username=username)
        followers = user.profile.followers.all()
        posts = user.profile.posts.all()
        description = user.profile.description
        return render(request, "posts/profile.html.dj",
                {'username':username,'user':user,'followers':followers,
                    'posts':posts, 'description':description})


    except User.DoesNotExist:
        return HttpResponse("Requested User {} does not exist".format(username))


def activity(request, username=None):
    return render(request, "posts/frame.html.dj", {'username':username})
