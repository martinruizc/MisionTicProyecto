from django.shortcuts import render, redirect,HttpResponse
from .models import Instructor
from .forms import InstructorForm

# Create your views here.
def main_page(request):
  return render(request, 'index.html')

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

# def delete_instrutor(request, id):
#   instructor = Instructor.objects.get(id=id)
#   if request.method == 'POST':
#     instructor.delete()
#     return redirect('instructor')



    
    
  
  
  