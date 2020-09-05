from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPI

class ImagesList(ListAPIView):
    serializer_class = AlbumImage

    def get_queryset(self):
        album = self.request.album

        if album:
            return AlbumImage.objects.filter(album=album)

        return AlbumImage.objects.all()
