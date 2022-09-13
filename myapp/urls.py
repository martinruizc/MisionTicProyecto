from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_page, name="index"),
  path('instructor/', views.instructor, name="instructor"),
  path('create_instructor/', views.create_instructor, name="create_instructor"),
  path('instructor/<int:id>', views.instructor_detail, name='instructor_detail'),
  path('instructor/<int:id>/delete', views.instructor_delete, name="instructor_delete"),
  path('signup/', views.sign_up, name="signup"),
  path('signout/', views.signout, name="signout"),
  path('signin/', views.signin, name="signin"),
  path('create_booking/' , views.create_booking, name='create_booking'),
  path('booking/', views.booking, name="booking"),
  path('booking/<int:id>/', views.booking_detail, name="booking_detail"),
  path('booking/<int:id>/delete', views.booking_delete, name="booking_delete")
]