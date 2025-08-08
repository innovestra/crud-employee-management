from django.urls import path
from .views import *

urlpatterns = [
    path('', employee_list, name='list'),
    path('create/', create_employee, name='create'),
    path('update/<int:id>/', update_employee, name='update'),
    path('delete/<int:id>/', delete_employee, name='delete'), # type: ignore
]
