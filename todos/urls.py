from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('addtodo/', views.addtodo, name = 'addtodo'),
    path('<int:todo_id>/delete_todo', views.deletetodo, name='deletetodo'),
    path('<int:todo_id>/editform', views.editform, name = 'editform'),
    path('<int:todo_id>/edittodo', views.edittodo, name= 'edittodo'),
]