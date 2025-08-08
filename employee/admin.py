from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_email', 'employee_phone', 'employee_hire_date', 'employee_job_title')
    search_fields = ('employee_name', 'employee_email', 'employee_job_title')
    list_filter = ('employee_hire_date', 'employee_job_title')

admin.site.register(Employee, EmployeeAdmin)