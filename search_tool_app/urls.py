from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'paper', views.PaperViewSet, basename="paper")
router.register(r'year', views.YearViewSet, basename="year")
router.register(r'tag', views.TagViewSet, basename="tag")
router.register(r'author', views.AuthorViewSet, basename="author")
router.register(r'type', views.TypeViewSet, basename="type")
router.register(r'language', views.LanguageViewSet, basename="language")
router.register(r'material', views.MaterialViewSet, basename="material")


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_a_publication/', views.post_a_publication, name='post_a_publication'),
    path('search_publication/', views.search_publication, name='search_publication'),
    path('show_publication/<slug:slug>/', views.show_publication, name='show_publication'),
    path('vue_example/', views.vue_example, name='vue_example'),
    path('vue_search/', views.vue_search, name='vue_search'),
    path('vue_paper_search/', views.vue_paper_search, name='vue_paper_search'),
] + router.urls
