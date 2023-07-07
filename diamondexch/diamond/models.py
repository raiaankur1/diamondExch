from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from datetime import datetime
# from django.contrib.auth.models import User as DjangoUser
# Create your models here.


# phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")
phone_validator = RegexValidator(
    r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$", "Invalid Phone Number")


class CustomUserManager(BaseUserManager):
    """
        create a new user
        @param username:  the name for the new user
        @param password:  the password for the new user. if none is provided a random password is generated
    """

    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('User must have a valid Phone Number')

        user = self.model(phone_number=phone_number, created=datetime.now(
        ))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = PhoneNumberField(validators=[phone_validator], unique=True)
    balance = models.IntegerField(default=0, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now())
    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number.as_e164

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True

    @property
    def is_staff(self):
        return self.is_superuser


# class User(AbstractBaseUser):
#     phone_number = PhoneNumberField(unique=True, primary_key=True)
#     password = models.CharField(max_length=20)
#     balance = models.IntegerField(default=0, null=False)

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = (password, balance)

#     def __str__(self):
#         return f"{self.phone_number}"

# class User(models.Model):
#     user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
#     phone_number = PhoneNumberField(unique=True)
#     password = models.CharField(max_length=20)
#     balance = models.IntegerField(default=0, null=False)

#     def __str__(self):
#         return f"{self.phone_number}"


class Gameid(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"


STATUS_CHOICES = (
    ("APPROVED", "APPROVED"),
    ("IN PROCESS", "IN PROCESS"),
    ("REJECTED", "REJECTED"),
)


class Depositstatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    utrno = models.CharField(default="", max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="IN PROCESS"
    )


class Withdrawstatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    upiid = models.CharField(default="", max_length=25)
    created_at = models.DateTimeField(
        auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="IN PROCESS"
    )
