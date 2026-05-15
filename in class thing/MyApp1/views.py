from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from datetime import datetime
from .models import teacher, courses, units, student
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO

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

def viewUnits()

def unit(request):
    unit = units.objects.all()

    return render(
        request, "MyApp1/units.html", {'content': unit}
        )

def students(request):
    students = student.objects.all()

    return render(
        request, "MyApp1/students.html", {'content': students}
        )

def report(request):
    pdf_file =  staticfiles_storage.path("DigitalSolutions.pdf")

    try:
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="attachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="no_attachment.pdf")
    return response

def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]

    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 0, 5)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer