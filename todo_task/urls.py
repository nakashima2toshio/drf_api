from django.urls import path

from todo_task.views import TaskAboutView
from todo_task.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('list', TaskListView.as_view(), name='task_list'),
    path('about', TaskAboutView.as_view(), name='about'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('update<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
