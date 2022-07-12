from django.shortcuts import render
from Evaluation.models import Relationship
from Evaluation.serializers import RelationshipSerializer,EmployeeSerializer,qaSerializer
from Employee.models import Employee
from QA.models import Question,Answer
from django.http import HttpRequest, HttpResponse, JsonResponse
import json


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
    length = len(all_questions_answers)
    final = []
    for i in range(0,length,2):
        x = {"q_id":all_questions_answers[i].id,"q_text":all_questions_answers[i].text,"answers":[]}
        final.append(x)
    af = []
    for j in all_questions_answers:
        keys = ["a_id","a_text"]
        d = dict.fromkeys(keys)
        d["a_id"] = j.answer_id
        d["a_text"] = j.answer_text
        af.append(d)
    x = 0 
    for i in range(len(final)):
        final[i]["answers"].append(af[x])
        x+=1
        final[i]["answers"].append(af[x])
        x+=1       
    #serializer = qaSerializer(all_questions_answers, many = True)
    return JsonResponse(final,safe=False)
