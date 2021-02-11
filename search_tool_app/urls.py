from django.urls import path
from search_tool_app import views

urlpatterns = [
    path('', views.homepage, name='homepage')
]
