
from requests import request
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskList(generics.ListAPIView):

    queryset = Task.objects.order_by('data')
    serializer_class = TaskSerializer


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



