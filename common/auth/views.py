from rest_framework import generics

from .models import CustomUser
from .serializers import UserSerializer

# from allauth.account.views import ConfirmEmailView
# from allauth.account.views import PasswordResetFromKeyView


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    # `from allauth.account.views import ConfirmEmailView` is importing the `ConfirmEmailView` class from
    # the `allauth` package, specifically from the `account.views` module. This class is typically used in
    # Django projects that utilize the django-allauth package for user authentication and account
    # management. The `ConfirmEmailView` is responsible for handling the email confirmation process for
    # user accounts, where users need to verify their email addresses before gaining full access to the
    # application.
    serializer_class = UserSerializer


# class CustomConfirmEmailView(ConfirmEmailView):
#     template_name = 'account/email_confirm.html'

# class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
#     template_name = 'account/password_reset_from_key.html'
