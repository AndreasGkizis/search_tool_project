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


urlpatterns = [] + router.urls
