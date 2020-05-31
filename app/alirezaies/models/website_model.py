from django.db import models

class WebsiteSettings(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return str(self.title)
