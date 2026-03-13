from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)

class courses(models.Model):
    Title = models.CharField(max_length=20)
    Code = models.CharField(max_length=10)