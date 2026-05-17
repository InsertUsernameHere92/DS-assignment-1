from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)

class courses(models.Model):
    Title = models.CharField(max_length=20)
    Code = models.CharField(max_length=10)

class units(models.Model):
    Title = models.CharField(max_length=20)
    Code = models.CharField(max_length=10)
    Assessment_Period = models.CharField(max_length=5)
    Course = models.ForeignKey(courses, on_delete=models.CASCADE)

class student(models.Model):
    Name = models.CharField(max_length=30)
    Student_ID = models.CharField(max_length=10)
    Year_Group = models.CharField(max_length=3)