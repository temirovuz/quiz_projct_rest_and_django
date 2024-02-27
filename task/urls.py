from django.urls import path

from .views import TaskModelCreate, TaskModelDetail


urlpatterns = [
    path('create', TaskModelCreate.as_view(), name='task_create'),
    path('<int:pk>', TaskModelDetail.as_view(), name='task_detail'),
]