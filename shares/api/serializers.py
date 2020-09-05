from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import *
from album.models import AlbumImage



class ImageSerializer(ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = [
            'id',
            'image',
            'alt'
        ]

class NewsListSerializer(ModelSerializer):
    preview = ImageSerializer(read_only=True)

    class Meta:
        model = News
        fields = (
            'uuid',
            'title',
            'preview',
            'slug',
            'announce',
            'created_at',
            'page_title',
            'is_shown'
        )


class NewsSerializer(ModelSerializer):
    preview = ImageSerializer(read_only=True)

    class Meta:
        model = News
        fields = (
            'uuid',
            'title',
            'preview',
            'created_at',
            'content',
            'page_title',
            'album',
            'is_shown'
        )


