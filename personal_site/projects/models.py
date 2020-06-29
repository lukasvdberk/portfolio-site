from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    short_description = models.CharField(max_length=1024, blank=False, null=False)
    long_description = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(max_length=256, blank=False, null=False)
    github_link = models.CharField(max_length=256, blank=False, null=True)
    date = models.DateField(blank=True, null=True)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField()


class Tag(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    icon = models.ImageField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
