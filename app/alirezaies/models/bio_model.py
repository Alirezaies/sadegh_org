from django.db import models

class Bio(models.Model):
    image_url = models.CharField(max_length=2048, null=True)
    bio = models.TextField(max_length=4000, null=True)
    name = models.CharField(max_length=32, null=True)
    role = models.CharField(max_length=32, null=True)
    dob = models.DateField(blank=False, null=True)
    nationality = models.CharField(max_length=32, null=True)

    def __str__(self):
        return str(self.name)
