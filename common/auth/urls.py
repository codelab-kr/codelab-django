# from allauth.account.views import PasswordResetView as AllauthPasswordResetView
# from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as v

app_name = 'account'

urlpatterns = [
    path('users/', v.UserListView.as_view(), name='user-list'),
    path('register/', v.SignUp.as_view(), name='register'),
    path('login/', v.Login.as_view(), name='login'),
    path('logout/', v.Logout.as_view(), name='logout'),
]
