from django.contrib import admin
from django.urls import path
from Project.views import mathOpe

urlpatterns = [
    path('home/<str:oper>/',mathOpe)
]
