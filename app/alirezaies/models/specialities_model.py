from django.db import models

class Specialities(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)