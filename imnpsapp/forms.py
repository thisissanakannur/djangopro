from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ngl(forms.ModelForm):
    class Meta:
        model=imnps
        fields='__all__'


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
