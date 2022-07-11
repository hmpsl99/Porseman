from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    creation_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text



