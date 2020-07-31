from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Building, MetaData, Document
from core.aws import create_presigned_url_expanded
from inspection.settings.dev import BUCKET_NAME


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ("id", "username", "password",)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"


class GetBuildingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Building
        fields = ("id",)


class MetaDataSerializer(serializers.ModelSerializer):
    building = GetBuildingSerializer()
    name = serializers.CharField(max_length=250, allow_null=True, allow_blank=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = MetaData
        fields = ('id', 'building', 'name', 'description')


class GetDocumentSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('get_bucket_urls', read_only=True)
    name = serializers.CharField(max_length=250, allow_null=True, allow_blank=True)
    building = GetBuildingSerializer()

    def get_bucket_urls(self, obj):
        url = create_presigned_url_expanded('get_object', method_parameters={'Bucket': BUCKET_NAME, 'Key': obj.name},
                                            expiration=3600, http_method='GET')
        return url

    class Meta:
        model = Document
        fields = ('id', 'building', 'name', 'url')


class DocumentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250, allow_null=True, allow_blank=True)
    building = GetBuildingSerializer()
    url = serializers.SerializerMethodField('put_bucket_urls', read_only=True)

    def put_bucket_urls(self, obj):
        url = create_presigned_url_expanded('put_object', method_parameters={'Bucket': BUCKET_NAME, 'Key': obj.name},
                                            expiration=3600, http_method='PUT')
        return url

    def create(self, validated_data):
        building_id = validated_data['building']['id']
        building_obj = Building.objects.get(pk=building_id)
        obj = Document.objects.create(building=building_obj, name=validated_data['name'])
        return obj

    class Meta:
        model = Document
        fields = ('building', 'name', 'url')
