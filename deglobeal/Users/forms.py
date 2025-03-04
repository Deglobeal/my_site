# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    second_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'second_name', 'last_name', 'address', 'email', 'password1', 'password2')