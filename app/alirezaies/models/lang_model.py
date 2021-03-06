from django.db import models

class Language(models.Model):

    name = models.CharField(max_length=32, unique=True)
    level = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)