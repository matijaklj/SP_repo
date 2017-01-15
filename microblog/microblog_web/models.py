from django.db import models

from django.conf import settings

from django.contrib.auth.models import User
from datetime import datetime, timedelta
from collections import Counter

from django.utils.translation import ugettext_lazy as _

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

"""
class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
"""

class ProfileManager(models.Manager):
    def create_profile(self, user, displayName):
        """
        returns new profile

        Keyword arguments:
            - self -- the profile object
            - user -- the User object
            - displayName -- the display name string
        """
        profile = self.create(user=user, displayName=displayName, description="")
        profile.following.add(profile) # vsak sam sebe followa
        return profile

class Profile(models.Model):
    """
    profile model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    displayName = models.CharField( max_length=30, blank=True, verbose_name=_("Display name"), default=User.username)
    description = models.CharField(max_length=150, default='', blank=True, verbose_name=_('Description'))
    coverImage = models.FileField(upload_to=user_directory_path, default='default/img/cover-image.jpg', blank=True, verbose_name=_("Cover image:"))
    profileImage = models.FileField(upload_to=user_directory_path, default='default/img/profile-image.jpg', blank=True, verbose_name=_("Profile image:"))
    following = models.ManyToManyField("self")

    objects = ProfileManager()

    def get_newsfeed(self):
        """
        returns post from profiles that the profile self follows

        Keyword arguments:
            - self -- the profile object
        """
        follow_profiles = self.following.all()
        #print({follow_profiles})
        return Post.objects.filter(profile__in=follow_profiles).order_by('-pub_date')

    def is_following(self, profile):
        """
        returns True if Profile self follows Profile profile else False

        Keyword arguments:
            - self -- the profile object
            - profile -- the profile object
        """
        s_fol = self.following.all()
        for p in s_fol:
            if p == profile:
                return True
        return False

    def follow(self, id):
        """
        adds the profile with the id (id) to the following profiles of self

        Keyword arguments:
            - self -- the profile object
            - id -- the id of the user of profile
        """
        profile1 = self
        profile2 = Profile.objects.get(user__id=id)
        if profile2:
            p1_following = profile1.following.all()
            for p in p1_following:
                if profile2 == p:
                    profile1.following.remove(profile2)
                    return True
            profile1.following.add(profile2)
            return True
        else:
            return False

    def delete(self):
        """
        deletes Profile object self

        Keyword arguments:
            - self -- the profile object
        """
        User.objects.get(id=self.user.id).delete()

class Hashtag(models.Model):
    """
    hashtag model
    """
    name = models.CharField(max_length=100, unique=True)

    def get_trending():
        """
        deletes Profile object self

        Keyword arguments:
            - self -- the profile object
        """
        posts_recent = Post.objects.filter(pub_date__gte = datetime.now() - timedelta(days=2))
        hashtags_list = []

        for post in posts_recent:
            post_hashtags = post.hashtags.all()
            for h in post_hashtags:
                hashtags_list.append(h)

        counter = Counter(hashtags_list).most_common()
        trending_hashtags_list = []
        for c in counter[:5]:
            trending_hashtags_list.append(c[0])

        return trending_hashtags_list


class PostManager(models.Manager):
    def create_post(self, profile, content, lat, lon):
        """
        creates and returns new post for the profile,
        with the conent and location specified.
        The function also creates hastags that are in
        the post content.

        Keyword arguments:
            - self -- the post object
            - profile -- the Profile object
            - content -- the conent od the post (string)
            - lat -- latitude of the location (double)
            - lon -- longitude of the location (double)
        """
        words = content
        hashtagSet = {ht[1:] for ht in words.split() if ht.startswith("#")}
        hashtag_list = []
        for h in hashtagSet:
            try:
                ht = Hashtag.objects.create(name=h.lower())
                hashtag_list.append(ht)
            except Exception as e:
                ht = Hashtag.objects.get(name=h.lower())
                hashtag_list.append(ht)
            else:
                pass

        post = self.create(profile=profile, content=content, location_lat=lat, location_lon=lon)
        for ht in hashtag_list:
            post.hashtags.add(ht)
        return post

class Post(models.Model):
    """
    post model
    """
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    hashtags = models.ManyToManyField('Hashtag')

    objects = PostManager()
