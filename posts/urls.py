from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns('',
    url(r'^user/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^user/(?P<username>\w+)/recent', views.activity, name='activity'),
)
