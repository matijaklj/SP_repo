from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from django.db.models import Count

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post, Profile, Hashtag #, Post_hashtag, Follow
from .forms import LoginForm, RegisterForm, NewPostForm, SearchForm, ProfileForm

from django.utils.translation import ugettext_lazy as _

def index(request):
    context = {}

    context['hashtags'] = Hashtag.get_trending()

    if not request.user.is_authenticated:
        posts = Post.objects.all().order_by('-pub_date')[:10]
    else:
        context['profile'] = Profile.objects.get(user = request.user)
        posts = Profile.get_newsfeed(context['profile'])#getPosts(request.user)

    context['posts'] = posts
    return render(request, 'microblog_web/index.html', context)
"""
def my_profile(request): # TODO to je kr neki preusmeri na profile/{this.user.id} al neki
    context = {}
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(profile = profile).order_by('-pub_date')

    context['profile'] = profile
    context['posts'] = posts

    return render(request, 'microblog_web/profile.html', context)
"""
def user_profile(request, id):
    context = {}
    context['profile'] = Profile.objects.get(user=request.user)

    profile = Profile.objects.get(user__pk = id)
    posts = Post.objects.filter(profile=profile).order_by('-pub_date')

    if request.user.is_authenticated:
        context['followed'] = Profile.is_following(Profile.objects.get(user=request.user), profile)
        #follow = #Follow.objects.get(user1=request.user, user2=profile.user)
        #if Profile.objects.is_following(request.user, profile):

    context['userprofile'] = profile
    context['posts'] = posts

    return render(request, 'microblog_web/profile.html', context)

def login_page(request):
    context = {}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/microblog')
            else:
                context['error'] = _("Incorrect username or password!")
        else:
            #return HttpResponseRedirect('/NOOOOthanks/')
            context['error'] = _("Incorrect username or password!")

    context['loginForm'] = LoginForm()
    return render(request, 'microblog_web/login.html', context)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/microblog')

def register_page(request):
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            displayName = form.cleaned_data['displayName']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if displayName == "":
                displayName = username
            if password1 == password2:
                try:
                    user =  User.objects.create_user(username, email, password1)
                    profile = Profile.objects.create_profile(user=user, displayName=displayName)

                    login(request, user)

                    return HttpResponseRedirect('/microblog/login')
                except Exception as e:
                    context['error'] = _("Username is already taken!")
                    pass
                else:
                    context['error'] = _("Username is already taken!")
                    pass
            else:
                context['error'] = _("Passwords must match!!!")
        else:
            context['error'] = _("Please fill all the marked fields")

    return render(request, 'microblog_web/register.html', context)

def newpost(request):
    if not request.method == 'POST':
        return HttpResponseRedirect('/microblog')

    form = NewPostForm(request.POST)
    profile = Profile.objects.get(user=request.user)

    if form.is_valid():
        content = form.cleaned_data['content']
        if form.cleaned_data['location_lat'] and form.cleaned_data['location_lon']:
            location_lat = float(form.cleaned_data['location_lat'])
            location_lon = float(form.cleaned_data['location_lon'])
        else:
            location_lat = None
            location_lon = None
        if not content == "":
            newpost = Post.objects.create_post(profile=profile, content=content, lat=location_lat, lon=location_lon)


    return HttpResponseRedirect('/microblog')

def hashtag_search(request, hashtag):
    context = {}
    context['profile'] = Profile.objects.get(user=request.user)
    context['posts'] = Post.objects.filter(hashtags__name=hashtag)

    return render(request, 'microblog_web/hashtag.html', context)

def followuser(request, id):
    profile = Profile.objects.get(user=request.user)
    Profile.follow(self=profile, id=id)
    return HttpResponseRedirect('/microblog/profile/' + str(id))

def search(request, search_str):
    context = {}
    context['profile'] = Profile.objects.get(user=request.user)
    context['posts'] = Post.objects.filter(content__icontains=search_str)
    return render(request, 'microblog_web/search.html', context)

def posts_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_str = form.cleaned_data['search_str']
            return HttpResponseRedirect('/microblog/search/' + search_str)

    return HttpResponseRedirect('/microblog')

def settings(request):

    if not request.user.is_authenticated:
        return  HttpResponseRedirect('/microblog/')
    else:
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():

                form_profile = form.save(commit=False)
                print(form_profile.coverImage)
                profile.description = form_profile.description
                profile.displayName = form_profile.displayName
                if form_profile.profileImage:
                    profile.profileImage = request.FILES['profileImage']
                if form_profile.coverImage:
                    profile.coverImage = request.FILES['coverImage']

                profile.save()
                #print(form_profile.user.id)

                return HttpResponseRedirect('/microblog/profile/' + str(request.user.id))

        context = {}
        context['EditProfile'] = ProfileForm(instance=profile) #EditProfileForm()
        context['profile'] = profile
        return render(request, 'microblog_web/settings.html', context)
