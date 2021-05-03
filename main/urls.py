from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', views.index),
    path('add/', views.add),
    path('addlead/', views.addlead),
    path('search/', views.search)
]
