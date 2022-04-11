from django.db import models
from user.models import User


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    booked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
