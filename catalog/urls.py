
from django.contrib import admin
from django.urls import path, include
from . import views, emp_views

urlpatterns = [
    path('index/', views.index),
    path('country/', views.country_info),
    path('add_publisher/', views.add_publisher),
    path('list_publishers/', views.list_publishers),
    path('employees/', emp_views.list_employees),
    path('addemployee/', emp_views.add_employee),
    path('deleteemployee/', emp_views.delete_employee),
    path('editemployee/', emp_views.edit_employee),
    path('searchemployees/', emp_views.search_employees),
    path('getemployees/', emp_views.get_employees),
    path('ajaxdemo/', views.ajax_demo),
    path('datetime/', views.send_datetime),

]
