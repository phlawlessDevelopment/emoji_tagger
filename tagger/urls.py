from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmojiViewSet, TagViewSet

router = DefaultRouter()
router.register('emoji', EmojiViewSet, basename='emoji')
router.register('tag', TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls))
]