from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(models.Model):
    phone_number = PhoneNumberField(unique=True)
    password = models.CharField(max_length=14)


class GameID(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
