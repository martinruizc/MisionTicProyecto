from types import CoroutineType
from django.forms import ModelForm
from django import forms
from .models import Instructor, Booking

class InstructorForm(forms.ModelForm):
  required_css_class = 'required-field'
  city = forms.CharField(widget=forms.TextInput(attrs={"typye": "text"}))
  description = forms.CharField(widget=forms.Textarea(attrs={"class": "description"}))
  class Meta:
    model = Instructor
    fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'description']

class BookingForm(forms.ModelForm):
  required_css_class = 'required-field'
  date = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "YYYY-MM-DD", "type": "date"}))
  hour = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
  class Meta:
    model = Booking
    fields = ['date', 'hour', 'place', 'instructor']