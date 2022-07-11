from django.shortcuts import render
from Evaluation.models import Relationship
from Evaluation.serializers import RelationshipSerializer,EmployeeSerializer,qaSerializer
from Employee.models import Employee
from QA.models import Question,Answer
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

def qa_api(request):
    query = 'select QA_question.id,QA_question.text ,QA_answer.id as answer_id,QA_answer.text as answer_text from QA_question join QA_answer on QA_answer.question_id =QA_question.id'
    all_questions_answers = Question.objects.raw(query)
    serializer = qaSerializer(all_questions_answers, many = True)
    return JsonResponse(serializer.data,safe=False)