from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # django-allauth URL 패턴 포함
]

if settings.DEBUG:
    urlpatterns += [path('__reload__/', include('django_browser_reload.urls'))]
