from . import views
from django.urls import path

urlpatterns = [
    path('',views.evaluation_page),
    path('relationships/',views.relationship_api),
    path('employees',views.employee_api),
    path('qa',views.qa_api),
    path('qa_new',views.qa_api_new),
    path('new',views.evaluation_page2),
]