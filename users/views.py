from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
from .models import Mentor
from django.views.generic.edit import CreateView


class UsersView(APIView):
    def get(self, request, *args, **kwargs):
        user_list = User.objects.all()
        user_serializer = UserSerializer(user_list, many=True)
        json_data = user_serializer.data
        return Response(json_data)
    
class MentorsView(APIView):
    def get(self, request, *args, **kwargs):
        mentor_list = Mentor.objects.all()
        mentor_serializer = MentorSerializer(mentor_list, many=True)
        json_data = mentor_serializer.data
        return Response(json_data)