from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutMeTagList.as_view()),
]
