from rest_framework import serializers
from task.models.task import *
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['user', 'phone_number']