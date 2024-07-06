from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('common.auth.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
    path('', include('services.blog.apps.post.urls')),
]
