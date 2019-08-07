from django.shortcuts import render
from .models import Employee


def  list_employees(request):
    return render(request,'list_employees.html',
                  {'employees': Employee.objects.all()})