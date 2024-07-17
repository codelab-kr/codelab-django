from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', include('common.auth.urls')),
    path('', include('services.blog.apps.post.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('__reload__/', include('django_browser_reload.urls'))]
