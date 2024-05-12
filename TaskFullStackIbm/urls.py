from django.urls import path

from Task.views import ListTasksView, AddTaskView, TaskDetailView, CompleteTaskView, DeleteTaskView

# URL patterns para enlazar vistas con URLs
urlpatterns = [
    path('', ListTasksView.as_view(), name='list_tasks'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('complete/<int:task_id>/', CompleteTaskView.as_view(), name='complete_task'),
    path('delete/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
]
