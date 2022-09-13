from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField()
  phone = models.CharField(max_length=250)
  city = models.TextField(max_length=250, default="Bogota")
  description = models.TextField()

  def __str__(self):
    return self.first_name + ' ' + self.last_name

  
class Booking(models.Model):
  booking_date = models.DateTimeField()
  place = models.CharField(max_length=150)
  instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  

