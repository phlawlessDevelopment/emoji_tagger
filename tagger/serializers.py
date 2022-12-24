from rest_framework import serializers

from .models import Emoji, Tag


class EmojiGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = '__all__'


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['value']


class EmojiCreateSerializer(serializers.ModelSerializer):
    tags = TagCreateSerializer(many=True)

    class Meta:
        model = Emoji
        fields = ['value', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        emoji = Emoji.objects.create(**validated_data)
        for tag_data in tags_data:
            tag = Tag.objects.create(**tag_data)
            emoji.tags.add(tag)
        return emoji


class TagGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
