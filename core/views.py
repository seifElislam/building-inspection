from rest_framework import viewsets
from django.contrib.auth.models import User
from core.models import Building, MetaData, Document
from core.serializer import UserSerializer, BuildingSerializer, MetaDataSerializer, DocumentSerializer, \
    GetDocumentSerializer
from core.filters import BuildingFilter, MetaDataFilter, DocumentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('building__name', 'building__address')
    filter_class = BuildingFilter


class MetaDataViewSet(viewsets.ModelViewSet):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('metadata__name',)
    filter_class = MetaDataFilter


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('document__name',)
    filter_class = DocumentFilter

    def get_serializer_class(self):
        """
        get the proper serializer
        :return proper serializer
        """
        if self.action == 'list' or self.action == 'retrieve':
            return GetDocumentSerializer
        return DocumentSerializer
