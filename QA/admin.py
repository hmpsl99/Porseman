from django.contrib import admin
from .models import Question,Answer
# Register your models here.
my_models = [Question,Answer]
admin.site.register(my_models)

