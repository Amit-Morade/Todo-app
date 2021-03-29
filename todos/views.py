from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from django.urls import reverse
# Create your views here.

def index(request):
    todo_list = Todo.objects.all()
    return render(request, 'todos/index.html',{'todo_list':todo_list})

def addtodo(request):
    new_todo = Todo(content = request.POST['content'])
    new_todo.save()
    return HttpResponseRedirect(reverse('todos:index'))

def deletetodo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todos:index'))

def editform(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    return render(request, 'todos/editform.html', {'todo':todo})

def edittodo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.content = request.POST['content']
    todo.save()
    return HttpResponseRedirect(reverse('todos:index'))
