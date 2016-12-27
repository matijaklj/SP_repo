from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    # todo dodaj profile_img, cover_img,...

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateField(default=datetime.now)
    # todo dodaj link, post_img, location,...


class Follow(models.Model):
    # user1 follows user2
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='is_followed_by')
