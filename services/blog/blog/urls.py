from django.urls import include, path

urlpatterns = [
    path('', include('common.auth.urls')),
    path('', include('services.blog.apps.post.urls')),
]
