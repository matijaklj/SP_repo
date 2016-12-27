from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Post

def index(request):
    return render(request, 'microblog_web/index.html', {'TEMPERATURE':'-0.5'})

def user_profile(request, id):
    context = {}
    user = User.objects.get(pk=id)
   # posts = Post.objects.get(user=user)

    context['user'] = user
    #context['posts'] = posts

    return render(request, 'microblog_web/profile.html', context)
