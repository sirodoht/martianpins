from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = "Martian Pins administration"
app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("terms", views.terms, name="terms"),
    path("pins/hash/", views.hash_pin, name="hash_pin"),
    path("pins/upload/", views.upload_pin, name="upload_pin"),
    path("pins/rm/<int:pin_id>", views.rm_pin, name="rm_pin"),
]
