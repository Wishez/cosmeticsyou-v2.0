from rest_framework.serializers import ModelSerializer, SlugRealtedField
from ..models import *



class NewsListSerializer(ModelSerializer):
    image = SlugRealtedField(
        read_only=True,
        slug_field="url"
    )

    class Meta:
        model = AlbumImage
        fields = (
            'image',
            'alt'
        )



