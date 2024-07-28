from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('mine/', views.ManageCourseListView.as_view(), name='manage_list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='delete'),
]
