from django.shortcuts import render,redirect
from .forms import EmployeeForm
from . import models
# Create your views here.
def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form  = EmployeeForm()
    return render(request, 'employee/employee.html', {'form': form})

def employee_list(request):
    employee = models.Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employee})

def update_employee(request, id):
    employee = models.Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/update_employee.html', {'form': form})

def delete_employee(request, id):
    employee = models.Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('list')