from django.urls import path
from .views import  helloWorld, taskList, yourName, taskView, newTask, editTask, deleteTask, changeStatus


urlpatterns = [
    path('helloworld/', helloWorld),
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name='task-view'),
    path('newtask/', newTask, name='new-task'),
    path('edit/<int:id>', editTask, name='edit-task'),
    path('changestatus/<int:id>', changeStatus, name='change-status'),
    path('delete/<int:id>', deleteTask, name='delete-task'),
    path('yourname/<str:name>', yourName, name='your-name' ),

]