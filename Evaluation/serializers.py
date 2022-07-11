from Employee.models import Employee
from rest_framework import serializers
from Evaluation.models import Relationship
from Employee.models import Employee


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','first_name']

class qaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    answer_id = serializers.IntegerField()
    answer_text = serializers.CharField()