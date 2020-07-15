from django.db import models


# Create your models here.
class AboutMeTag(models.Model):
    about_me = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.about_me