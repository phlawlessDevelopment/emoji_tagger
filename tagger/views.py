from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from .models import Emoji, Tag
from .serializers import EmojiCreateSerializer, EmojiGetSerializer, TagGetSerializer
from random import choices


class EmojiViewSet(viewsets.ModelViewSet):

    def get_queryset(self):

        count = self.request.query_params.get('count', 4)
        types = self.request.query_params.get('types')

        if types == 'tagged':
            emoji = Emoji.objects.annotate(
                tag_count=Count('tags')).filter(tag_count__gt=0)
            if emoji.all().count() == 0:
                return []
            else:
                return choices(emoji, k=int(count))

        elif types == 'untagged':
            emoji = Emoji.objects.annotate(
                tag_count=Count('tags')).filter(tag_count=0)
            if emoji.all().count() == 0:
                return []
            else:
                return choices(emoji, k=int(count))

        elif types == 'mixed':
            return choices(Emoji.objects.all(), k=int(count))

    def get_serializer_class(self):
        if self.action == 'create':
            return EmojiCreateSerializer
        else:
            return EmojiGetSerializer
    

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagGetSerializer
