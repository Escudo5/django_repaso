from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Task
from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')
def products(request):
    return render(request, 'accounts/products.html')
def customer(request):
    return render(request, 'accounts/customer.html')

def create_task(request):
    return render(request, 'accounts/create_task.html')

#def get_tasks(request):
    if (request.method == "GET"):
        lista = list(Task.objects.all().values())
        return JsonResponse(lista, safe=False) 
    

class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#Una vista de las tareas en forma de lista

class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = {
        'title' : ['icontains', 'exact']
    }

# COnfigura las apis para poder hacer CRUD(Create, Read, Update, Delete)