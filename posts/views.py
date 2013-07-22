from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from posts.models import UserProfile, Post

def index(request):
    return render(request,"posts/frame.html.dj")

def profile(request, username):
    try: 
        user = UserProfile.objects.get(user__username=username)
        current_user = request.session.get('username', None)
        if current_user == user.usgr.username:
            return HttpResponseRedirect(reverse('posts:me'))
        else:
            followers = user.followers.all()
            posts = user.posts.order_by('createdDate')[:7]
            return render(request, "posts/profile.html.dj",
                    {'current_user':current_user,'user':user,
                        'followers':followers,'posts':posts.reverse(),
                        })


    except UserProfile.DoesNotExist:
        return HttpResponse("Requested User {} does not exist".format(username))


def activity(request):
    current_user = request.session.get(username, 'False')
    if current_user:
        user = UserProfile.objects.get(user__username=current_username)

def me(request):
    current_username = request.session.get('username', False)
    if current_username:
        user = UserProfile.objects.get(user__username=current_username)
        if request.method == 'POST':
            c = {}
            c.update(csrf(request))
            post_text = request.POST['post_text']
            post = Post.objects.create(user=user, content=post_text)
            post.save()
            return HttpResponseRedirect(reverse('posts:me'), c)
        else:
            posts = user.posts.order_by('createdDate')[:7]
            following = user.following.all()
            return render(request, "posts/me.html.dj",{'user':user,
                'posts':posts.reverse(), 'following':following, 
                'current_user':current_username})
    else:
        return HttpResponseRedirect(request, 'login')
