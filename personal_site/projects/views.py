from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer


class ProjectList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

