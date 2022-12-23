from django.urls import path
from .views import tag_mode

urlpatterns = [
    path('', tag_mode, name='tag-mode'),
]