from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns('',
    url(r'^user/me/$', views.me, name='me'),
    url(r'^user/(?P<username>\S+)/$', views.profile, name='profile'),
)
