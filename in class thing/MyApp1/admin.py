from django.contrib import admin
from .models import teacher
from .models import courses

# Register your models here.
admin.site.register(teacher)
admin.site.register(courses)