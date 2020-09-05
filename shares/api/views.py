# -*- encoding: utf-8 -*-
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *

class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'

class NewsView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_field = 'slug'
