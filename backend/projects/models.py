from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from django.template.defaultfilters import slugify

PROJECT_SIZES = [
    ('LARGE', 'large'),
    ('MEDIUM', 'medium'),
    ('SMALL', 'small'),
]


class Project(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    short_description = models.CharField(max_length=1024, blank=False, null=False)
    long_description = MarkdownxField(blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField(max_length=256, blank=False, null=False)
    github_link = models.URLField(max_length=256, blank=False, null=True)
    date = models.DateField(blank=True, null=True)
    size = models.CharField(
        choices=PROJECT_SIZES,
        max_length=64,
        null=False,
        blank=False,
        default='SMALL'
    )

    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.project.name


class Tag(models.Model):
    project = models.ForeignKey(Project, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False)
    icon = models.ImageField()

    def __str__(self):
        return self.name
