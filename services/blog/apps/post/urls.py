from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('create/', views.post_create, name='create'),
]
