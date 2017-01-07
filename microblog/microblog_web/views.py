from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .models import Post
from .forms import LoginForm

def index(request):
    context = {}

    # if not loged in then display most recent posts
    if not request.user.is_authenticated:
        posts = Post.objects.all().order_by('-pub_date')[:5]


    context['posts'] = posts
    return render(request, 'microblog_web/index.html', context)

def user_profile(request, id):
    context = {}
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(user=user).order_by('-pub_date')

    context['user'] = user
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
