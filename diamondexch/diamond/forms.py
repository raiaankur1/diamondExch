from django.forms import ModelForm, TextInput, PasswordInput
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

from .models import *


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        # phone_number.widget.attrs.update({"class": "register_input"})
        # widgets = {
        #     'phone_number': TextInput(attrs={'class': 'register_input', 'type': 'text', 'placeholder': "Phone Number"}),
        #     'password': PasswordInput(attrs={'class': 'register_input', 'type': 'password', 'placeholder': 'Password'}),
        # }


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['password']
        # phone_number.widget.attrs.update({"class": "register_input"})
        widgets = {
            # 'phone_number': TextInput(attrs={'class': 'register_input', 'type': 'text', 'placeholder': "Username"}),
            'password': PasswordInput(attrs={'class': 'register_input', 'type': 'password', 'placeholder': 'Password'}),
        }


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=14, widget=forms.TextInput(
        attrs={'class': 'register_input', 'type': 'text', 'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'register_input', 'type': 'password', 'placeholder': 'Password'}))
