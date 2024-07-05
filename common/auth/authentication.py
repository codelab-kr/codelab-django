from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not user.is_active:
            raise AuthenticationFailed('User is inactive or deleted.')
        return (user, token)
