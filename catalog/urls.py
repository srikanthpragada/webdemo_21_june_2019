
from django.contrib import admin
from django.urls import path, include
from . import views, emp_views, rest_views,class_views

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
    path('rest/employees/', rest_views.employees_get_post),
    path('rest/employees/<int:id>', rest_views.process_one_employee),
    path('rest/client/', rest_views.client),
    path('about/', class_views.AboutView.as_view()),
    path('emps/', class_views.ListEmployeesView.as_view()),

]
