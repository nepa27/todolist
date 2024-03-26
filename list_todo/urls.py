from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('list/', views.ToDoListView.as_view(), name='list'),
    path('add_todo/', views.AddToDoView.as_view(), name='add'),
    path('update_todo/', views.UpdateToDoView.as_view(), name='update'),
    path('delete_todo/', views.DeleteToDoView.as_view(), name='delete'),
    path('list/<int:todo_pk>', views.DetailToDoView.as_view(), name='delete'),
]
