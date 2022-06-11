from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.TaskList.as_view(), name="task-list"),
    path('api/create', views.TaskCreate.as_view(), name="task-create"),
  ]
