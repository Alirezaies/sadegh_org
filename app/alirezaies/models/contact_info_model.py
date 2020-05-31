from django.db import models

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return_value = str(self.address) + '-' + str(self.phone_number) + '-' + str(self.email)

        return str(return_value)
