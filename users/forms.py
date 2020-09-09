from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'user_type','password1', 'password2']