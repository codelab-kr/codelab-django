from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('', include('common.auth.urls')),
    path('', include('services.edu.apps.courses.urls')),
    path('students/', include('services.edu.apps.students.urls')),
    path('chat/', include('services.edu.apps.chat.urls', namespace='chat')),
    path('api/', include('services.edu.apps.courses.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
