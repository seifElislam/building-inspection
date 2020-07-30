"""inspection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from inspection.settings.dev import SWAGGER_URL

API_INFO = openapi.Info(
    title="TruScore API",
    default_version='v1.2',
    description="TruScore API ",
)
SchemaView = get_schema_view(url=SWAGGER_URL,
                             public=False,
                             permission_classes=(permissions.IsAdminUser,))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('core.urls')),
    path('swagger/', login_required(SchemaView.with_ui('swagger', cache_timeout=1))),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
