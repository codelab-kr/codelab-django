from django.urls import path

from . import views

# app_name = 'course'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('course/mine/', views.ManageCourseListView.as_view(), name='course_manage_list'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('course/<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/<pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path(
        'module/<int:module_id>/content/<model_name>/create/',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_create'
    ),
    path(
        'module/<int:module_id>/content/<model_name>/<id>/',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_update'
    ),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
    path('module/order/', views.ModuleOrderView.as_view(), name='module_order'),
    path('content/order/', views.ContentOrderView.as_view(), name='content_order'),
    path('subject/<slug:subject>/', views.CourseListView.as_view(), name='course_list_subject'),
    path('course/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]
