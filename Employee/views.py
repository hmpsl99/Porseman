from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Employee import serializers
from Employee.models import Employee
from Employee.serializers import employeeserializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

def all_employees(request):
    query = 'select Employee_employee.id,  Employee_employee.first_name, Employee_position.name from Employee_employee join Employee_position on Employee_position.id = Employee_employee.position_id'
    all_employees = Employee.objects.raw(query)
    serializer = employeeserializer(all_employees, many = True)
    return JsonResponse(serializer.data,safe=False)
