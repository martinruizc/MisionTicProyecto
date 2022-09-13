from syslog import closelog
from django.forms import ModelForm, DateInput
from .models import Instructor, Booking

class InstructorForm(ModelForm):
  class Meta:
    model = Instructor
    fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'description']

class BookingForm(ModelForm):
  class Meta:
    model = Booking
    fields = ['booking_date', 'place', 'instructor']
