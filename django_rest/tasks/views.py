from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
class TaskView(viewsets):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()