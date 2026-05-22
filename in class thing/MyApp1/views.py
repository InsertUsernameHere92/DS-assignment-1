from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from datetime import datetime
from .models import teacher, courses, units, student
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO
#from lxml import etree, html

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

def outline(request):
    unit = units.objects.all()

    return render(
        request, "MyApp1/outline.html", {'content': unit}
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

#def generate_html_pdf(html_path = outline.html):
    #with open(html_path, "r", encoding="utf-8") as f:
        #html_content = f.read()

    #tree = html.fromstring(html_content)
    #styles = getSampleStyleSheet()
    #doc = SimpleDocTemplate(out_path, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    #story = []

    # Title
    #h1 = tree.xpath("//h1/text()")
    #if h1:
        #story.append(Paragraph(h1[0], styles["Title"]))
        #story.append(Spacer(1, 6 * mm))

    # Invoice meta (example mapping for two-column rows)
    #meta_rows = []
    #for tr in tree.xpath("//table[contains(@class, 'details')][1]//tr"):
        #tds = [td.text_content().strip() for td in tr.xpath("./td")]
        #if len(tds) == 2:
            #meta_rows.append([tds[0], tds[1]])
    #if meta_rows:
        #meta_tbl = Table(meta_rows, colWidths=[80 * mm, 80 * mm])
        #meta_tbl.setStyle(TableStyle([
            #("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F7F7F7")),
            #("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#DDDDDD")),
            #("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#DDDDDD")),
            #("FONT", (0, 0), (-1, -1), "Helvetica", 10),
        #]))
        #story.append(meta_tbl)
        #story.append(Spacer(1, 6 * mm))

    # Items table (assuming the second .details table contains items)
    #item_table = tree.xpath("//table[contains(@class, 'details')][2]")
    #if item_table:
        #rows = []
        #for tr in item_table.xpath(".//tr"):
            #cells = [td.text_content().strip() for td in tr.xpath("./td")]
            #if cells:
                #rows.append(cells)
        #item_tbl = Table(rows, colWidths=[100 * mm, 40 * mm])
        #item_tbl.setStyle(TableStyle([
            #("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EEEEEE")),
            #("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CCCCCC")),
            #("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            #("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        #]))
        #story.append(item_tbl)
        #story.append(Spacer(1, 6 * mm))

    # Totals
    #total_text = tree.xpath("//table[contains(@class, 'totals')]//strong/parent::td/text()")
    #if total_text:
        #story.append(Paragraph(f"<b>Total:</b> {total_text[0].strip()}", styles["Normal"]))

    #doc.build(story)

