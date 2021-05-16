from datetime import datetime

from django.shortcuts import render, redirect
from .forms import Register, LoginUser, NewBlog
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Blog, SiteConfiguration
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import BlogSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_blog_list(request):
    blog_list = Blog.objects.all()
    serializer = BlogSerializer(blog_list, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def blog_detail(request, pk):
    try:
        single_blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        if pk:
            serializer = BlogSerializer(single_blog)
            return JsonResponse(serializer.data, safe=False)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BlogSerializer(single_blog, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        single_blog.delete()
        return HttpResponse(status=204)


def index(request):
    blog_data = Blog.objects.all().order_by('-last_modified')
    paginator_object = Paginator(blog_data, 6)
    page_data = paginator_object.get_page(request.GET.get('page', 1))
    return render(request, 'myblog/home.html', {"page_data": page_data,
                                                "site_conf": SiteConfiguration.objects.get(pk=1)})


def profile(request, username=None):
    blog_data = Blog.objects.filter(user_name=username).order_by('-last_modified')
    paginator_object = Paginator(blog_data, 6)
    page_data = paginator_object.get_page(request.GET.get('page', 1))
    return render(request, 'myblog/home.html', {"page_data": page_data,
                                                "site_conf": SiteConfiguration.objects.get(pk=1)})


def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Registration successful, kindly login again.")
            return redirect("login")
    else:
        form = Register()
    return render(request, "myblog/register.html", {"registration_form": form,
                                                    "site_conf": SiteConfiguration.objects.get(pk=1)})


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
    return render(request, "myblog/login.html", {"login_form": form,
                                                 "site_conf": SiteConfiguration.objects.get(pk=1)})


def new_blog(request):
    if request.method == "POST":
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            blog_object = Blog()
            blog_object.blog_title = form.cleaned_data.get('blog_title')
            blog_object.blog_description = form.cleaned_data.get('blog_description')
            blog_object.blog_user_id = request.user
            blog_object.creation_date = datetime.now()
            blog_object.last_modified = datetime.now()
            blog_object.user_name = request.user
            blog_object.blog_image = request.FILES['blog_image']
            blog_object.save()
            messages.success(request, "New blog created")
    else:
        form = NewBlog()
    return render(request, "myblog/new_blog.html", {"new_blog": form,
                                                    "site_conf": SiteConfiguration.objects.get(pk=1)})


def blog(request, blog_id):
    if request.method == "POST":
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            blog_object = Blog.objects.get(pk=blog_id)
            blog_object.blog_title = form.cleaned_data.get('blog_title')
            blog_object.blog_description = form.cleaned_data.get('blog_description')
            blog_object.blog_user_id = request.user
            blog_object.last_modified = datetime.now()
            blog_object.blog_image = request.FILES['blog_image']
            blog_object.save()
            messages.success(request, "Blog updated successfully")
    else:
        current_blog = Blog.objects.get(pk=blog_id)
        init_dict = {
            "blog_title": current_blog.blog_title,
            "blog_description": current_blog.blog_description,
            "last_modified": current_blog.last_modified
        }
        current_blog.views = current_blog.views + 1
        current_blog.save()
        form = NewBlog(initial=init_dict)

    return render(request, "myblog/blog.html", {"new_blog": form,
                                                "site_conf": SiteConfiguration.objects.get(pk=1)})
