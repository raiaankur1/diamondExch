from django.forms import ModelForm, TextInput, PasswordInput
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

from .models import *


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        # phone_number.widget.attrs.update({"class": "register_input"})
        widgets = {
            'phone_number': TextInput(attrs={'class': 'register_input', 'type': 'text', 'placeholder': "Username"}),
            'password': PasswordInput(attrs={'class': 'register_input', 'type': 'password', 'placeholder': 'Password'}),
        }
