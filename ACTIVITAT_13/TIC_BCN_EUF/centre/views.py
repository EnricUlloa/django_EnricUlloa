from re import template

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Student, Teacher

# Create your views here.

def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'index.html', {'students': students, 'teachers': teachers})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})

def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})