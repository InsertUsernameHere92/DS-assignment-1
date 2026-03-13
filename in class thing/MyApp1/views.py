from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher

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