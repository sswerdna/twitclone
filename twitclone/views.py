from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from posts.models import UserProfile

def login_page(request):
    if request.method == "POST":
        c = {}
        c.update(csrf(request))
        username=request.POST['username']
        password=request.POST['password']
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logout(request)
                return HttpResponseRedirect(reverse("posts:activity", args =(username,)))
            else:
                return HttpResponse("Auth Failed, bad pass")
        except KeyError:
            return HttpResponse("Auth Failed, bad username")
    else:
        return render(request, 'posts/login.html.dj')
        #return HttpResponse("Please Log In")

def create(request):
    if request.method == 'POST':
        c = {}
        c.update(csrf(request))
        username = request.POST['username']
        if not User.objects.filter(username=username):
            passw = request.POST['password']
            if not passw == request.POST['verify']:
                return HttpResponse("Passwords don't match!")
            else:
                user = User.objects.create_user(username,
                        request.POST['email'],
                        )
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.set_password(passw)
                user.save()
                profile = UserProfile(user=user,description=request.POST['description'])
                profile.save()
                return HttpResponseRedirect(reverse("posts:activity", args=(username,)))
        else:
            return HttpResponse("Username Taken!")
    else:
        return render(request, 'posts/create.html.dj')
