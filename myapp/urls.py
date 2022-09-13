from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_page, name="index"),
  path('instructor/', views.instructor, name="instructor"),
  path('create_instructor/', views.create_instructor, name="create_instructor"),
  path('instructor/<int:id>', views.instructor_detail, name='instructor_detail'),
  path('signup/', views.sign_up, name="signup"),
  path('signout/', views.signout, name="signout"),
  path('signin/', views.signin, name="signin")
]