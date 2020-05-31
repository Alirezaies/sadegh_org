from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=4000)

    def __str__(self):
        return str(self.subject)
