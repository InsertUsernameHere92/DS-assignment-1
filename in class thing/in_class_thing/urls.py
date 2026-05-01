from django.urls import include, re_path
import MyApp1.views
from django.contrib import admin
from django.urls import path

"""
in_class_thing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('teachers/', MyApp1.views.teachers, name='teachers'),
    path('courses/', MyApp1.views.course, name='courses'),
    re_path(r'^$', MyApp1.views.index, name='index'),
    re_path(r'^home$', MyApp1.views.index, name='home'),
]
