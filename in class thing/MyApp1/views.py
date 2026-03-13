from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .models import courses

# Create your views here.
def index(request):
    return render(
        request,"MyApp1/index.html"
        )

def teachers(request):
    teach = teacher.objects.all()

    return render(
        request,"MyApp1/teachers.html", {'content': teach}
        )

def course(request):
    course = courses.objects.all()

    return render(
        request, "MyApp1/courses.html", {'content': course}
        )