from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=255, unique=False)
    role = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.company