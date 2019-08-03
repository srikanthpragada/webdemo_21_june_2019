from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    job = models.CharField(max_length=15)
    salary = models.IntegerField()
    email = models.EmailField(max_length=50)

