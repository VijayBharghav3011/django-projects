from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt

from .serializers import TaskSerializers
from .models import TaskList
# rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(['GET'])
def task_name(request):
    api_links = {
        'tasklist': 'task-list/',
        'particular-task': 'get-task-info/<id>',
        'create task': 'create-task/',
        'update-task': 'update-task/<id>',
        'delete-task': 'delete-task/<id>',
    }
    return Response(api_links)


@api_view(['GET'])
def taskList(request):
    task = get_list_or_404(TaskList.objects.order_by('id'))
    serializer = TaskSerializers(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, id):
    task = get_object_or_404(TaskList, id=id)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateTask(request, id):
    task = get_object_or_404(TaskList, id=id)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTask(request, id):
    task = get_object_or_404(TaskList, id=id)
    task.delete()
    return Response('Task Deleted')
