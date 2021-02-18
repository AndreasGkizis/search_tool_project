from django.urls import path
from search_tool_app import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_a_publication/', views.post_a_publication, name='post_a_publication')
]
