from django.shortcuts import render
from Evaluation.models import Relationship
from Evaluation.serializers import RelationshipSerializer,EmployeeSerializer
from Employee.models import Employee
from django.http import HttpResponse, JsonResponse


# Create your views here.
def relationship_api(request):
    all_relationships = Relationship.objects.all()
    serializer = RelationshipSerializer(all_relationships, many = True)
    return JsonResponse(serializer.data,safe=False)

def evaluation_page(request):
    return render(request, 'Evaluation/evaluation.html')

def employee_api(request):
    all_employees = Employee.objects.all().values('first_name')
    serializer = EmployeeSerializer(all_employees,many = True)
    return JsonResponse(serializer.data,safe=False)