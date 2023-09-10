from django.db import models

# Create your models here.

class Registers(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    re_password = models.CharField(max_length=128)
    def __str__(self):
        return self.username