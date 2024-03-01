from django.urls import path
from crud_app import views


urlpatterns = [
   path('',views.task_list,name='task_list'),
   path('details/<int:id>/', views.task_details,name='task_details'),
   path('create/',views.create_tasks,name='create_tasks'),
   path('edit/<int:id>/',views.edit_task,name='edit_task'),
   path('delete/<int:id>/',views.delete_task,name='delete_task'),
]
