from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q




class PhoneUsernameAuthenticationBackend(object):
    @staticmethod
    def authenticate(request, phone_number=None, password=None):
        try:
            user = get_user_model().objects.get(
                Q(phone_number=phone_number)
            )

        except get_user_model().DoesNotExist:
            print("doesn't exist")
            return None

        if user and check_password(password, user.password):
            return user

        return None

    @staticmethod
    def get_user(user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
