from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'paper', views.PaperViewSet)

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_a_publication/', views.post_a_publication, name='post_a_publication'),
    path('search_publication/', views.search_publication, name='search_publication'),
    path('show_publication/<slug:slug>/', views.show_publication, name='show_publication'),
    path('vue_example/', views.vue_example, name='vue_example'),
    path('vue_search/', views.vue_search, name='vue_search'),
    path('type/', views.TypeView.as_view(), name='type_view'),
    path('vue_paper_search/', views.vue_paper_search, name='vue_paper_search'),
    # path('paper/', views.PaperViewSet.as_view(), name='paper_view')
] + router.urls
