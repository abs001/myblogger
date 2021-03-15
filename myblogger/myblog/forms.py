from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUser(forms.Form):
    username = forms.CharField(label="User Name", max_length=150, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter your Username"}))
    password1 = forms.CharField(label="Password", max_length=150, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter your Password"}))


class NewBlog(forms.Form):
    blog_title = forms.CharField(label="Form Title", max_length=250, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter title here"}
    ))
    blog_description = forms.CharField(label="Blog Description", widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Enter blog Description"}
    ))
