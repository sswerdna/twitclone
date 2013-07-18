from django.conf.urls import patterns, include, url
from twitclone import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', views.login),
    url(r'^posts/', include('posts.urls')),
)
