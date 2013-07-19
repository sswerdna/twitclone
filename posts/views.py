from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from posts.models import UserProfile, Post

def index(request):
    return render(request,"posts/frame.html.dj")

def profile(request, username):
    try: 
        user = User.objects.get(username=username)
        current_user = request.session.get('username', None)
        if current_user == user.username:
            return HttpResponseRedirect(reverse('posts:me'))
        else:
            followers = user.profile.followers.all()
            posts = user.profile.posts.order_by('createdDate')[:7]
            description = user.profile.description
            return render(request, "posts/profile.html.dj",
                    {'current_user':current_user,'user':user,
                        'followers':followers,'posts':posts,
                        'description':description})


    except User.DoesNotExist:
        return HttpResponse("Requested User {} does not exist".format(username))


def activity(request, username=None):
    return render(request, "posts/frame.html.dj", {'username':username})

def me(request):
    current_username = request.session.get('username', False)
    if current_username:
        if request.method == 'POST':
            pass
        else:
            user = User.objects.get(username=current_username)
            posts = user.profile.posts.order_by('createdDate')[:7]
            following = user.profile.following.all()
            return render(request, "posts/me.html.dj",{'user':user,
                'posts':posts, 'following':following, 
                'current_user':user.username})
    else:
        return HttpResponseRedirect(request, 'login')
