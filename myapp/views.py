from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Instructor
from .forms import InstructorForm
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
      return redirect('index')
      

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
    'form': form
    })
  
  else:
    instructor = Instructor.objects.get(id=id)
    form = InstructorForm(request.POST, instance=instructor)
    form.save()
    #return redirect(f'instructor')
    return redirect('instructor')





    
  
  
  