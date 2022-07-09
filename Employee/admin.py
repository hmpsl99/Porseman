from django.contrib import admin
from .models import Employee,Department,Team,Position
# Register your models here.
my_models = [Employee,Department,Team,Position]
admin.site.register(my_models)
