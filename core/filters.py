"""
Filters for all models
"""

from django_filters import rest_framework as filters
from core.models import Building, MetaData, Document


class BuildingFilter(filters.FilterSet):

    """
    building Filter Set
    """
    name_contains = filters.CharFilter(field_name="name", lookup_expr='icontains')
    address_contains = filters.CharFilter(field_name="address", lookup_expr='icontains')

    class Meta:
        model = Building
        fields = [
            'name',
            'name_contains',
            'address',
            'address_contains',
        ]


class MetaDataFilter(filters.FilterSet):

    """
    building Filter Set
    """
    name_contains = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = MetaData
        fields = [
            'name',
            'name_contains'
        ]


class DocumentFilter(filters.FilterSet):

    """
    building Filter Set
    """
    name_contains = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Document
        fields = [
            'name',
            'name_contains'
        ]