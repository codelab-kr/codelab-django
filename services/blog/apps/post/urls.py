from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('get_verse/', views.get_verse, name='get_verse'),
    path('book_autocomplete/', views.book_autocomplete, name='book_autocomplete'),
    path('search/', views.search_view, name='search'),
]
