from . import views
from django.urls import path

urlpatterns = [
    path('',views.evaluation_page),
    path('relationships/',views.relationship_api),
    path('employees',views.employee_api),
]