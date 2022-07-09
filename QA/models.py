from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=500)
    creation_time = models.DateTimeField(default=timezone.now)


class Answer(models.Model):
    text = models.CharField(max_length=500)
    creation_time = models.DateTimeField(default=timezone.now)



