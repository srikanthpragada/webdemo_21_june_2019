
from django.contrib import admin
from django.urls import path, include

from . import views, emp_views

urlpatterns = [
    path('index/', views.index),
    path('country/', views.country_info),
    path('add_publisher/', views.add_publisher),
    path('list_publishers/', views.list_publishers),
    path('employees/', emp_views.list_employees)

]
