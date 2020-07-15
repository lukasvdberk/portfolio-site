from django.contrib import admin
from .models import *
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.
admin.site.register(Project, MarkdownxModelAdmin)
admin.site.register(ProjectImage)
admin.site.register(Tag)
