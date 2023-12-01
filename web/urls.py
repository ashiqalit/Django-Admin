from django.urls import path, include
from django.contrib import admin
from web import views
urlpatterns = [
    path ('', views.index, name = 'web'),
]