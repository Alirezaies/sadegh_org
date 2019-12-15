from django.db import models

class SocialLinks(models.Model):
    name = models.CharField(max_length=32, unique=True)
    link = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=64)

    def __str__(self):
        return self.name