from django.db import models

class Bio(models.Model):
    image_url = models.CharField(max_length=2048)
    bio = models.TextField(max_length=4000)
    name = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    dob = models.DateField(null=False, blank=False)
    nationality = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)
