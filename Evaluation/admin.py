from django.contrib import admin
from .models import Evaluation,Relationship,Results
from import_export.admin import ExportActionMixin

# Register your models here.
#class EvaluationAdmin(ExportActionMixin, admin.ModelAdmin):
#    list_display = ('user_logged_in', 'reviewee', 'relationship', 'question','answer','creation_time')

admin.site.register(Evaluation)
admin.site.register(Relationship)

@admin.register(Results)
class ResultsAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['evaluation_id','reviewee_last_name','question_category','question','reviewee_own_answer','reviewee_own_answer_score','other_avg','difference','department_avg']
    list_filter = ['reviewee_last_name', 'evaluation_id']
