from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.pagination import PageNumberPagination


class ProjectList(generics.ListAPIView):
    filterset_fields = ['size', 'slug']
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination
    ordering_fields = ['size']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

