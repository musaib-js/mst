from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length = 250)
    subject = models.CharField(max_length = 350)
    phone = models.CharField(max_length = 250)
    message = models.TextField()

    def __str__(self):
        return self.name
    

