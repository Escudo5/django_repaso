from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from models import Task

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')
def products(request):
    return render(request, 'accounts/products.html')
def customer(request):
    return render(request, 'accounts/customer.html')

def create_task(request):
    return render(request, 'accounts/create_task.html')