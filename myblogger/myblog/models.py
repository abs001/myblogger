from django.db import models
from django.conf import settings


class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=200)
    site_address = models.TextField()
    site_logo = models.ImageField()
    social_fb = models.CharField(max_length=200)
    social_li = models.CharField(max_length=200)
    social_tw = models.CharField(max_length=200)


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField()
    blog_image = models.ImageField()  # Future scope
    blog_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    views = models.IntegerField(default=0)
    user_name = models.TextField(default="Admin")
