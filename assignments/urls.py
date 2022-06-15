from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("" , views.assignmentshome, name = "assignhome"),
    path("<str:unique_name>/", views.assignmentview, name = "assignmentview"),
]
