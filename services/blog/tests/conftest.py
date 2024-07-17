import pytest
from django.contrib.auth import get_user_model

# fields = ('username', 'email', 'phone_number', 'password1', 'password2')


@pytest.fixture
def user1():
    return get_user_model().objects.create_user('testuser1', 'test@test.com', 'my-secret')
