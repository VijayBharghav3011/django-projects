from .views import task_name, taskList, taskDetail, createTask,updateTask, deleteTask
from django.urls import path

urlpatterns = [
    path('task-name', task_name, name='task_name'),
    path('task-list/', taskList, name='task_list'),
    path('get-task-info/<id>', taskDetail, name='get_task'),
    path('create-task/', createTask, name='create_task'),
    path('update-task/<id>', updateTask, name='update_task'),
    path('delete-task/<id>', deleteTask, name='delete_task'),
]