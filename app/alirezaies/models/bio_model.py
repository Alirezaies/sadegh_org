from django.db import models

class Bio(models.Model):
    image_url = models.CharField(max_length=2048, default='https://avatars3.githubusercontent.com/u/16784257?s=460&v=4')
    bio = models.TextField(max_length=4000)

    def __str__(self):
        return self.bio