from django.shortcuts import render
from Evaluation.models import Relationship
from Evaluation.serializers import RelationshipSerializer,EmployeeSerializer,qaSerializer
from Employee.models import Employee
from QA.models import Question,Answer
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from Evaluation.models import Evaluation,Relationship


# Create your views here.
def relationship_api(request):
    all_relationships = Relationship.objects.all()
    serializer = RelationshipSerializer(all_relationships, many = True)
    return JsonResponse(serializer.data,safe=False)

def evaluation_page(request):
    return render(request, 'Evaluation/evaluation.html')

def employee_api(request):
    all_employees = Employee.objects.all().values('id','first_name')
    serializer = EmployeeSerializer(all_employees,many = True)
    return JsonResponse(serializer.data,safe=False)
    
@csrf_protect
def qa_api(request):
    if request.method == "GET":
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
                #persian font problem solved.
                #a = json.dumps(final, ensure_ascii=False)       
                #serializer = qaSerializer(all_questions_answers, many = True)
                return JsonResponse(final,safe=False, json_dumps_params={'ensure_ascii': False})
    if request.method == "POST":
                evaluation_serie = request.user
                evaluations = json.loads(request.body)
                for evaluation in evaluations:
                    rev = Employee.objects.get(id=evaluation['e_id'] )
                    rel = Relationship.objects.get(id = evaluation['r_id'] )
                    qu = Question.objects.get(id = evaluation['qu_id'])
                    an = Answer.objects.get(id = evaluation['ans_id'])
                    new_record = Evaluation(user_logged_in = evaluation_serie,reviewee=rev,relationship=rel ,question=qu,answer =an)
                    new_record.save()

                return JsonResponse("OK",safe=False)
    #return HttpResponse(a)
