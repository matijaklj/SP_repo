from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from django.db.models import Count

from django.contrib.auth import authenticate, login, logout, models

from .models import Post, Profile, Follow, Hashtag, Post_hashtag
from .forms import LoginForm, RegisterForm, NewPostForm

def getPosts(user):
    posts = None
    if not user is None:
        following = Follow.objects.filter(user1=user)
        fol_list = []
        for f in following:
            p = Profile.objects.get(user = f.user2)
            fol_list.append(p.pk)
        posts = Post.objects.filter(profile__pk__in=fol_list).order_by('-pub_date')[:15]
    else:
        posts = Post.objects.all().order_by('-pub_date')[:10]
    return posts

def getTrending():
    ph = Post_hashtag.objects.filter(date__gte = datetime.now() - timedelta(days=2)).values("hashtag").annotate(Count('hashtag_id')).order_by('-hashtag_id__count')[:5]
    hashtags = []
    print(ph.query)
    for h in ph:
        hashtags.append(Hashtag.objects.get(pk=h['hashtag']))
    return hashtags


def index(request):
    context = {}

    context['hashtags'] = getTrending()

    #Follow.objects.create_follow(user1=request.user,user2=request.user)
    # if not loged in then display most recent posts
    if not request.user.is_authenticated:
        #posts = Post.objects.all().order_by('-pub_date')[:10]
        posts = getPosts(None)
        #print ({posts[0].profile.user})
    else:
        context['profile'] = Profile.objects.get(user = request.user)
        posts = getPosts(request.user)
        """
        following = Follow.objects.filter(user1=request.user)
        fol_list = []
        for f in following:
            p = Profile.objects.get(user = f.user2)
            fol_list.append(p.pk)

        #print(fol_list)
        posts = Post.objects.filter(profile__pk__in=fol_list)[:15]
        """


    context['posts'] = posts
    return render(request, 'microblog_web/index.html', context)

def my_profile(request):
    context = {}
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(profile = profile).order_by('-pub_date')

    context['profile'] = profile
    context['posts'] = posts

    return render(request, 'microblog_web/profile.html', context)

def user_profile(request, id):
    context = {}
    #user = User.objects.get(pk=id)
    profile = Profile.objects.get(user__pk = id)
    posts = Post.objects.filter(profile=profile).order_by('-pub_date')

    context['profile'] = profile
    context['posts'] = posts

    return render(request, 'microblog_web/profile.html', context)

def login_page(request):
    context = {}
    # todo login stuff
    # if this is a POST request we need to process the form data
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
                context['error'] = "Incorrect username or password!"
        else:
            return HttpResponseRedirect('/NOOOOthanks/')
            context['error'] = "Incorrect username or password!"

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
                    user = User.objects.create_user(username, email, password1)
                    profile = Profile.objects.create_profile(user=user, displayName=displayName)

                    login(request, user)

                    Follow.objects.create(request.user, request.user)

                    return HttpResponseRedirect('/microblog')
                except Exception as e:
                    raise
                else:
                    pass

        return HttpResponseRedirect('/microblog')

    return render(request, 'microblog_web/register.html', context)

def newpost(request):
    if not request.method == 'POST':
        return HttpResponseRedirect('/microblog')

    form = NewPostForm(request.POST)
    profile = Profile.objects.get(user=request.user)

    if form.is_valid():
        content = form.cleaned_data['content']

        if not content == "":
            words = content
            hashtagSet = {ht[1:] for ht in words.split() if ht.startswith("#")}
            hashobj = []
            for h in hashtagSet:
                try:
                    ht = Hashtag.objects.create(name=h.lower())
                    hashobj.append(ht)
                except Exception as e:
                    ht = Hashtag.objects.get(name=h.lower())
                    hashobj.append(ht)
                else:
                    pass

            newpost = Post.objects.create_post(profile=profile, content=content)

            for h in hashobj:
                Post_hashtag.objects.create(post=newpost, hashtag=h)

    return HttpResponseRedirect('/microblog')

def hashtag(request, ht):
    context = {}
    try:
        hashtagobj = Hashtag.objects.get(name=ht)
        if hashtagobj:
            post_hashtag = Post_hashtag.objects.filter(hashtag=hashtagobj)
            posts = []
            print(post_hashtag)
            for ph in post_hashtag:
                print(ph.post)
                posts.append(ph.post)
            context['posts'] = posts
    except Exception as e:
        pass


    return render(request, 'microblog_web/hashtag.html', context)
