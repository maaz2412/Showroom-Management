from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Showroom(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null =True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)
    def __str__(self):
        return self.name
