from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

def login(request):
    if request.method == "POST":
        try:
            user = authenticate(request.post['username'],request.post['password'])
            if user is not None:
                return HttpResponse("Logged in {}".format(request.post['username']))
            else:
                return HttpResponse("Auth Failed")
        except KeyError:
            return HttpResponse("Auth Failed")
    else:
        return render(request, 'posts/login.html.dj')
        #return HttpResponse("Please Log In")
