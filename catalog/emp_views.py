from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Employee
from .forms import EmployeeForm


def search_employees(request):
    return render(request, 'search_employees.html')

def get_employees(request):
    name = request.GET['name']  # Querystring with name
    emps = Employee.objects.filter(fullname__contains=name)
    # convert Queryset of Employee objects to list of dict
    emplist = list(emps.values())
    return JsonResponse(emplist,safe = False)



def list_employees(request):
    return render(request, 'list_employees.html',
                  {'employees': Employee.objects.all()})


def add_employee(request):
    if request.method == "GET":
        f = EmployeeForm()
        return render(request, 'add_employee.html', {"form": f})
    else:
        f = EmployeeForm(request.POST)
        if f.is_valid():
            f.save()  # insert row into table
            return redirect('/catalog/employees/')

        return render(request, 'add_employee.html', {"form": f})


def delete_employee(request):
    id = request.GET['id']
    # Get employee by the given id
    try:
        e = Employee.objects.get(id=id)
        print("Got employee : ", e)
        e.delete()
        return redirect("/catalog/employees/")
    except Exception as ex:
        print("Error in delete employee : ", ex)
        message = "Sorry! Could not delete employee!"
        return render(request, 'delete_employee.html',
                      {'message': message})


def edit_employee(request):
    if request.method == "GET":
        id = request.GET['id']
        # Get employee by the given id
        try:
            e = Employee.objects.get(id=id)
            f = EmployeeForm(instance=e)
            return render(request, 'edit_employee.html',
                          {'form': f})
        except Exception as ex:
            print("Error in edit employee : ", ex)
            message = "Sorry! Could not find employee!"
            return render(request, 'edit_employee.html',
                          {'message': message})
    else:

        e = Employee.objects.get(id=request.GET['id'])
        f = EmployeeForm(request.POST, instance=e)
        if f.is_valid():
            f.save()  # Updation
            return redirect("/catalog/employees")
        else:
            return render(request, 'edit_employee.html',
                          {'form': f,
                           'message': 'Invalid Data. Please correct and resubmit'})
