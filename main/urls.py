from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = "Martian Pins administration"
app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
]
