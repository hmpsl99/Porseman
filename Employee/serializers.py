from rest_framework import serializers

class employeeserializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    position = serializers.CharField()