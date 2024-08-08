from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserListView

# app_name = 'api'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('auth/', obtain_auth_token, name='auth'),
]
