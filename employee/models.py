from django.db import models
import random
from datetime import datetime
# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True, blank=True)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField(unique=True)
    employee_phone = models.CharField(max_length=10, unique=True)
    employee_hire_date = models.DateField()
    employee_job_title = models.CharField(max_length=100)
    
    def generate_employee_id(self):
        """Generate employee ID in format: EMP-12345, 2023-HR-007"""
        # Part 1: EMP
        prefix = "EMP"
        
        # Part 2: Random 5-digit number
        random_num1 = random.randint(10000, 99999)
        
        # Part 3: Employment year (from hire date)
        employment_year = self.employee_hire_date.year
        
        # Part 4: Role abbreviation based on job title
        role_mapping = {
            'human resources': 'HR',
            'hr': 'HR',
            'manager': 'MGR',
            'developer': 'DEV',
            'engineer': 'ENG',
            'analyst': 'ANL',
            'designer': 'DES',
            'accountant': 'ACC',
            'sales': 'SAL',
            'marketing': 'MKT',
            'operations': 'OPS',
            'finance': 'FIN',
            'administration': 'ADM',
            'admin': 'ADM',
            'executive': 'EXE',
            'consultant': 'CON',
            'specialist': 'SPE',
            'coordinator': 'COR',
            'assistant': 'AST',
            'support': 'SUP',
            'technician': 'TEC'
        }
        
        # Extract role from job title
        job_title_lower = self.employee_job_title.lower()
        role = 'GEN'  # Default role if not found
        
        for key, value in role_mapping.items():
            if key in job_title_lower:
                role = value
                break
        
        # Part 5: Random 3-digit number
        random_num2 = random.randint(100, 999)
        
        # Format: EMP-12345, 2023-HR-007
        employee_id = f"{prefix}-{random_num1}, {employment_year}-{role}-{random_num2:03d}"
        
        return employee_id
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            # Generate unique employee ID
            while True:
                new_id = self.generate_employee_id()
                if not Employee.objects.filter(employee_id=new_id).exists():
                    self.employee_id = new_id
                    break
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.employee_name} ({self.employee_id})"