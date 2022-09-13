from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Instructor, Booking
from .forms import InstructorForm, BookingForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def main_page(request):
  return render(request, 'index.html')

def sign_up(request):
  if request.method == 'GET':
    return render(request, 'signup.html', {
      'form': UserCreationForm
    })
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('index')
      except:
        return render(request, 'signup.html',{
          'form': UserCreationForm,
          'error': 'username is alredy in used, try a new one'
        })
    else:
      return render(request, 'signup.html', {
        'form': UserCreationForm,
        'error': 'Password does\'t match'
      })

def signout(request):
  logout(request)
  return redirect('index')      

def signin(request):
  if request.method == 'GET':
    return render(request, 'signin.html', {
      'form': AuthenticationForm
    })
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    
    if user is None:
      return render(request, 'signin.html', {
        'form': AuthenticationForm,
        'error': 'Invalid credentials'
      })
    else:
      login(request, user)
      return redirect('booking')
      

def instructor(request):
  instructor = Instructor.objects.all()
  return render(request, 'instructor.html',{
    'instructors': instructor
  })


def create_instructor(request):
  if request.method == 'GET':
    return render(request, 'create_instructor.html', {
    'form': InstructorForm()})
  else: 
    Instructor.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], phone=request.POST['phone'], city=request.POST['city'], description=request.POST['description'])
    return redirect('instructor')

def instructor_detail(request, id):
  if request.method == 'GET' :
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(instance=instructor)
    return render(request, 'instructor_detail.html', {
    'form': form,
    'instructor': instructor
    })
  
  else:
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(request.POST, instance=instructor)
    form.save()
    #return redirect(f'instructor')
    return redirect('instructor')

def instructor_delete(request, id):
  instructor = Instructor.objects.get(id=id)
  if request.method == "POST":
    instructor.delete()
    return redirect('instructor')

def create_booking(request):
  if request.method == 'GET':
    return render(request, 'create_booking.html', {
      'form': BookingForm()
    })
  else:
    form = BookingForm(request.POST)
    new_booking = form.save(commit=False)
    new_booking.user = request.user
    new_booking.save()
    return redirect('booking')

def booking(request):
  booking = Booking.objects.filter(user_id=request.user)
  return render(request, 'booking.html', {
    'booking': booking
  })

def booking_detail(request, id):
  if request.method == 'GET':
    booking = Booking.objects.get(id=id)
    form = BookingForm(instance=booking)
    return render(request, 'booking_detail.html',{
      'form': form,
      'booking': booking
    })
  else:
    booking = Booking.objects.get(id=id)
    form = BookingForm(request.POST, instance=booking)
    form.save()
    return redirect('booking')

def booking_delete(request, id):
  booking = Booking.objects.get(id=id)
  if request.method == 'POST':
    booking.delete()
    return redirect('booking')


    
  
  
  