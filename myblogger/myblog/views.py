from django.shortcuts import render, redirect
from .forms import Register, LoginUser, NewBlog
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    context = {}
    return render(request, 'myblog/home.html', context)


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Registration successful, kindly login again.")
            return redirect("login")
    else:
        form = Register()
    return render(request, "myblog/register.html", {"registration_form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.add_message(request, messages.INFO, "Logged in successfully")
                return redirect('/')
            else:
                form = LoginUser()
                messages.add_message(request, messages.ERROR, "Invalid credentials!")
    else:
        form = LoginUser()
    return render(request, "myblog/login.html", {"login_form": form})


def new_blog(request):
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data.get('blog_title')
            blog_description = form.cleaned_data.get('blog_description')
            form.save()
    else:
        form = NewBlog()
    return render(request, "myblog/new_blog.html", {"new_blog": form})
