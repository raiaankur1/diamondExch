from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(models.Model):
    phone_number = PhoneNumberField(unique=True)
    password = models.CharField(max_length=20)
    balance = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f"{self.phone_number}"


class Gameid(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"
