from django.contrib import admin
from .models import Employee,Department,Team,Position
# Register your models here.
my_models = [Department,Team,Position]
admin.site.register(my_models)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','position','team','parent','creation_time','department']
    sortable_by = ['first_name', 'last_name','position','team','parent','creation_time','department']
    list_filter = ['first_name', 'last_name','position','team','parent','creation_time','department'] 
    search_fields = ['first_name','last_name']
    fields = [('first_name', 'last_name'), 'position','team','parent','creation_time','department']
