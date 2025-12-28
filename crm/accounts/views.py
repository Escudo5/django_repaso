from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Task
from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet

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


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer