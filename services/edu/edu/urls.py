from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from services.edu.apps.courses import views

urlpatterns = [
    path('', include('common.auth.urls')),
    path('', views.CourseListView.as_view(), name='course_list'),
    path('', include('services.edu.apps.courses.urls')),
    path('students/', include('services.edu.apps.students.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
