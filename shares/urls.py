from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', SharesView.as_view(), name='shares'),
]

