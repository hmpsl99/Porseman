from django.contrib import admin
from .models import Question,Answer,Category_new,Question_new,Answer_new
# Register your models here.
my_models = [Question,Answer,Category_new,Question_new,Answer_new]
admin.site.register(my_models)

