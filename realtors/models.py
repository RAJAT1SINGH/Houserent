from django.db import models
from datetime import datetime

# Create your models here.
class Agents(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name