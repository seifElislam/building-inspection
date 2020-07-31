from rest_framework import viewsets
from django.contrib.auth.models import User
from core.models import Building, MetaData, Document
from core.serializer import UserSerializer, BuildingSerializer, MetaDataSerializer, DocumentSerializer, \
    GetDocumentSerializer, RegistrationSerializer
from core.filters import BuildingFilter, MetaDataFilter, DocumentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status


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


@api_view(['POST', ])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('saved')
            return Response({'msg':'account is created'})
        else:
            return Response({'msg': serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)

