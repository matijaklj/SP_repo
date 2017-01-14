"""fri_ws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<id>[0-9]+)/$', views.user_profile, name='profile'),
    url(r'^login', views.login_page, name='login'),
    url(r'^logout', views.logout_page, name='logout'),
    url(r'^register', views.register_page, name='register'),
    url(r'^newpost', views.newpost, name='newpost'),
    url(r'^hashtag/(?P<hashtag>[\w]+)/', views.hashtag_search, name='hashtagSearch'),
    url(r'^follow/(?P<id>[0-9]+)/$', views.followuser, name='follow'),
    url(r'^search/([\w]+)', views.search),
    url(r'^search$', views.posts_search, name='search'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^delete/profile$', views.delete_profile, name='delete_profile'),
    url(r'^delete/post$', views.delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
