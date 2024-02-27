import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from task.serializers import TaskCreateSerializer, TaskDetailSerializer
from task.models import Task


class TaskModelCreate(APIView):
    def post(self, request, format=None):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskModelDetail(APIView):
    def get(self, request, pk):
        task = Task.objects.filter(pk=pk).first()
        time.sleep(5)
        task.status = 'prosessing'
        task.save()
        time.sleep(5)
        task.status = 'finished'
        task.save()
        serializer = TaskDetailSerializer(task)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
