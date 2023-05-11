from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'password']

