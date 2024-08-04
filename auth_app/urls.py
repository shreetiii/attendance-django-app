from django.contrib import admin
from django.urls import path
from auth_app import views

urlpatterns = [
    path('', views.display),
]
