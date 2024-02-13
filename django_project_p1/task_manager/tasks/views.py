#from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, TaskMember
from .serializers import TaskSerializer, TaskMemberSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskMemberViewSet(viewsets.ModelViewSet):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer

# Create your views here.
