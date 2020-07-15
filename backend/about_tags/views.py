from rest_framework import generics
from .serializers import AboutMeTagSerializer
from .models import AboutMeTag
from rest_framework.pagination import PageNumberPagination


class AboutMeTagList(generics.ListAPIView):
    queryset = AboutMeTag.objects.all()
    serializer_class = AboutMeTagSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

