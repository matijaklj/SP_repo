from django.db import models

from django.contrib.auth.models import User
from datetime import datetime


class ProfileManager(models.Manager):
    def create_profile(self, user, displayName):
        profile = self.create(user=user, displayName=displayName, description="")
        return profile

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    displayName = models.CharField(max_length=30)
    description = models.CharField(max_length=150, default='')
    # todo dodaj profile_img, cover_img,...
    coverImage = models.CharField(max_length=100, default='microblog/img/cover-image.jpg')
    profileImage = models.CharField(max_length=100, default='microblog/img/profile-image.jpg')
    objects = ProfileManager()

class PostManager(models.Manager):
    def create_post(self, profile, content):
        post = self.create(profile=profile, content=content)
        return post

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    # todo dodaj link, post_img, location,...
    objects = PostManager()

class FollowManager(models.Manager):
    def create_follow(self, user1, user2):
        follow = self.create(user1=user1, user2=user2)
        return follow

class Follow(models.Model):
    # user1 follows user2
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='is_followed_by')
    objects = FollowManager()

class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post_hashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
