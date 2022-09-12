from django.forms import ModelForm
from .models import Instructor

class InstructorForm(ModelForm):
  class Meta:
    model = Instructor
    fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'description']

