from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField(max_length=3, primary_key=True)
    username = models.CharField(max_length=200, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
