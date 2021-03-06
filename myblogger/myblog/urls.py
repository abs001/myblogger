from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('register', views.register, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('new_blog', views.new_blog, name="new_blog"),
    path('blog/<int:blog_id>', views.blog, name="blog"),
    path('get_blog_list', views.get_blog_list),
    path('blog_detail/<int:pk>', views.blog_detail)
]