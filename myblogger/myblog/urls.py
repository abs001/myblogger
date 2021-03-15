from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('new_blog', views.new_blog, name="new_blog")
]