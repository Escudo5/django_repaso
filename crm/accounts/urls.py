from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('customer/', views.customer),
    path('products/', views.products),
    path('create_task/', views.create_task)


]