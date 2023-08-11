from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class LogoutForm(forms.Form):
    pass

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_role')
