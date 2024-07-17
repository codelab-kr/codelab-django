from django.contrib import admin
from django.urls import include, path  # , re_path

from .views import UserListView

# from .views import CustomConfirmEmailView
# from allauth.account import views as account_views

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # django-allauth URL 패턴 포함
    # path('accounts/confirm-email/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    # 비밀번호 재설정
    # re_path(r'^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', CustomPasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
    # path('accounts/password/reset/key/done/', account_views.password_reset_from_key_done, name='account_reset_password_from_key_done'),
]
