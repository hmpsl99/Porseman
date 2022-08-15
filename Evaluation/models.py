from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from QA.models import Question,Answer
from Employee.models import Employee
from django.utils import timezone
from dbview.models import DbView
# Create your models here.
class Relationship(models.Model):
    title = models.CharField(max_length=100)
    score_weight = models.IntegerField(default=0)
    def __str__(self):
        return self.title
class Evaluation(models.Model):
    user_logged_in = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return  str(self.question) + ' - ' + str(self.answer)

class Results(models.Model):
    evaluation_id = models.CharField(max_length=100)
    reviewee_last_name = models.CharField(max_length=100)
    question_category = models.CharField(max_length=100)
    question = models.CharField(max_length=30000)
    reviewee_own_answer = models.CharField(max_length=30000)
    reviewee_own_answer_score = models.FloatField()
    other_avg = models.FloatField()
    difference = models.FloatField()
    department_avg =  models.FloatField()

    class Meta:
        managed = False
        db_table = "results"