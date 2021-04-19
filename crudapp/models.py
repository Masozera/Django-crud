from django.db import models

# Create your models here.
class Student(models.Model):  
    sid = models.CharField(max_length=20)  
    name    = models.CharField(max_length=100)  
    email   = models.EmailField()  
    contact = models.CharField(max_length=15)  
    marks   = models.CharField(max_length=15)
    