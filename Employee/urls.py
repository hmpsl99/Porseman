from . import views
from django.urls import path

urlpatterns = [
    path('employees/',views.all_employees_api),
    path('',views.all_employees),
]