from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_a_publication/', views.post_a_publication, name='post_a_publication'),
    path('search_publication/', views.search_publication, name='search_publication')
]
