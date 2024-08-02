from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # django-allauth URL 패턴 포함
    path('accounts/edit/', edit, name='account_edit'),
    path('api/', include('common.auth.api.urls')),
    path('__debug__/', include('debug_toolbar.urls'))  # django-debug-toolbar
]

if settings.DEBUG:
    urlpatterns += [path('__reload__/', include('django_browser_reload.urls'))]
