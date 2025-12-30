from django.urls import path, include
from . import views
from .views import TaskListAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', views.TaskModelViewSet)

urlpatterns = [
    path('', views.home),
    path('customer/', views.customer),
    path('products/', views.products),
    path('create_task/', views.create_task),
    #path('tasks/', views.get_tasks),
    #path('api/tasks/', views.TaskListAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),



]