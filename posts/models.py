from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    description = models.TextField()
    following = models.ManyToManyField("self",symmetrical=False,
            related_name='followers')
    createdDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{}'s Profile".format(self.user)

class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='posts')
    content = models.CharField(max_length=140)
    createdDate = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return "Post created by {} on {:!s}".format(self.user,self.createdDate)
