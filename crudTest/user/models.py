from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256, default='', blank=False)
    password = models.CharField(max_length=256, blank=False, default='')
