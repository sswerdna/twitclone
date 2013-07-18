from django.conf.urls import patterns, include, url
from twitclone import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', views.login_page, name='login'),
    url(r'^create/$', views.create, name='create'),
    url(r'^posts/', include('posts.urls', namespace="posts")),
)
