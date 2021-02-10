from django.urls import path
from search_tool import views

urlpatterns = [
    path('', views.homepage, name='homepage')
]
