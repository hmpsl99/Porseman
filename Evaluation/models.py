from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from QA.models import Question,Answer
from Employee.models import Employee
from django.utils import timezone
# Create your models here.
class Relationship(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Evaluation(models.Model):
    user_logged_in = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)