from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.addTask, name='addTask'),
    path('mark-as-done/<int:pk>', views.mark_as_done, name='mark_as_done'),
    path('mark-as-undone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),
    path('edit-task/<int:pk>', views.editTask, name='editTask'),
    # path('update-task/<int:pk>', views.updateTask, name='updateTask'),
    path('delete-task/<int:pk>', views.deleteTask, name='deleteTask')
]
