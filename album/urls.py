from django.conf.urls import url
from .api.views import *

urlpatterns = [
    url(r'', ImagesList.as_view(), name="album_images")
]


