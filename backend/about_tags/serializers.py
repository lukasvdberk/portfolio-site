from django.conf.urls import url, include
from rest_framework import serializers
from .models import AboutMeTag


class AboutMeTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeTag
        fields = '__all__'
