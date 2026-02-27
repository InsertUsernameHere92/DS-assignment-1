from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)