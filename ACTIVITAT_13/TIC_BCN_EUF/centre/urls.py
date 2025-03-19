from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='students'),
    path('teachers/', views.teacher_list, name='teachers'),
    path("student/<int:id>/", views.student_detail, name="student_detail"),
    path("teacher/<int:id>/", views.teacher_detail, name="teacher_detail"),
]