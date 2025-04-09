from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import UserAuthentication


class BackendMailVerification(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):

        if email:
            try:
                user = UserAuthentication.objects.get(email=email)
            except UserAuthentication.DoesNotExist:
                return None
        elif username:
            try:
                user = UserAuthentication.objects.get(username=username)
            except UserAuthentication.DoesNotExist:
                return None
        else:
            return None

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):

        try:
            return UserAuthentication.objects.get(pk=user_id)
        except UserAuthentication.DoesNotExist:
            return None
