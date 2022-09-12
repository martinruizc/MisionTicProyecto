from django.db import models

# Create your models here.

class Instructor(models.Model):
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField()
  phone = models.CharField(max_length=250)
  city = models.TextField(max_length=250, default="Bogota")
  description = models.TextField()
  
