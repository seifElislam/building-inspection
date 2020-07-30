from rest_framework.routers import DefaultRouter
from core.views import UserViewSet

USER_ROUTER = DefaultRouter()
USER_ROUTER.register(r'users', UserViewSet, basename='User')

USERS_URLS = USER_ROUTER.urls
urlpatterns = []
urlpatterns += USERS_URLS
