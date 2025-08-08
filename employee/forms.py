from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_email', 'employee_phone', 'employee_hire_date', 'employee_job_title']
