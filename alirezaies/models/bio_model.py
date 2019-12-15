from django.db import models

class Bio(models.Model):
    bio = models.TextField(max_length=4000)

    def __str__(self):
        return self.bio