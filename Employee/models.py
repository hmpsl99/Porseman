from django.db import models
from django.utils import timezone
# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
class Department(models.Model):
    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name


class Team(models.Model):
    department = models.ForeignKey(Department ,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=30,null=True, blank=True , default = 'ali')
    last_name = models.CharField(max_length=30,null=True, blank=True, default = 'ali')
    position = models.ForeignKey( Position ,on_delete=models.CASCADE)
    team = models.ForeignKey(Team ,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete= models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE , default=1)
    def __str__(self):
        return self.first_name+self.last_name



