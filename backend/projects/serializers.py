from django.conf.urls import url, include
from rest_framework import serializers
from .models import Project, ProjectImage, Tag
from personal_site import settings


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = ProjectImage
        fields = ['image']


class TagSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    def get_icon(self, obj):
        return obj.icon.url

    class Meta:
        model = Tag
        fields = ['name', 'icon']


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
