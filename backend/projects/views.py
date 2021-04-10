# Create your views here.
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Project
from .serializers import ProjectSerializer


class ProjectList(generics.ListAPIView):
    filterset_fields = ['size', 'slug']
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.queryset.order_by('-date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

