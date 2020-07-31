from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, BuildingViewSet, MetaDataViewSet, DocumentViewSet, registration_view

USER_ROUTER = DefaultRouter()
USER_ROUTER.register(r'users', UserViewSet, basename='User')

BUILDING_ROUTER = DefaultRouter()
BUILDING_ROUTER.register(r'buildings', BuildingViewSet, basename='Building')

METADATA_ROUTER = DefaultRouter()
METADATA_ROUTER.register(r'metadata', MetaDataViewSet, basename='Metadata')

DOCUMENT_ROUTER = DefaultRouter()
DOCUMENT_ROUTER.register(r'document', DocumentViewSet, basename='Document')

USERS_URLS = USER_ROUTER.urls
BUILDINGS_URLS = BUILDING_ROUTER.urls
METADATA_URLS = METADATA_ROUTER.urls
DOCUMENT_URLS = DOCUMENT_ROUTER.urls


urlpatterns = [path(r'api/register/', registration_view, name='register')]
urlpatterns += USERS_URLS
urlpatterns += BUILDINGS_URLS
urlpatterns += METADATA_URLS
urlpatterns += DOCUMENT_URLS
