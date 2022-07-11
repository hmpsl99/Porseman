from django.contrib import admin
from .models import Evaluation,Relationship
# Register your models here.
#class EvaluationAdmin(ExportActionMixin, admin.ModelAdmin):
#    list_display = ('user_logged_in', 'reviewee', 'relationship', 'question','answer','creation_time')

admin.site.register(Evaluation)
admin.site.register(Relationship)