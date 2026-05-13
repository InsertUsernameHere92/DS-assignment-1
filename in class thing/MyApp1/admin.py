from django.contrib import admin
from .models import teacher, courses, units, student

# Register your models here.
admin.site.register(teacher)
admin.site.register(courses)
admin.site.register(units)
admin.site.register(student)