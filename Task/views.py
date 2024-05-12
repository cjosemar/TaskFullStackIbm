from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from Task.forms import TaskForm
from Task.models import Task


# Vista para agregar una nueva tarea
class AddTaskView(View):
    # Crea un formulario vacío para añadir una nueva tarea
    def get(self, request):
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})

    # Procesa el formulario rellenado para añadir una nueva tarea
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'add_task.html', {'form': form})


# Vista para mostrar todas las tareas
class ListTasksView(View):
    # Obtiene el filtro desde la URL, por defecto muestra todas las tareas
    def get(self, request):
        filter_task = request.GET.get('filter', 'all')
        if filter_task == 'completed':
            tasks = Task.objects.filter(completed=True)
        elif filter_task == 'pending':
            tasks = Task.objects.filter(completed=False)
        else:
            tasks = Task.objects.all()
        return render(request, 'list_tasks.html', {'tasks': tasks, 'filter': filter_task})


# Vista de detalle de la tarea
class TaskDetailView(View):
    def get(self, request, task_id):
        # Muestra el formulario con los detalles de la tarea existente para editar
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'form': form, 'task_id': task_id})

    def post(self, request, task_id):
        # Actualiza la tarea en la base de datos tras la edición
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'task_detail.html', {'form': form, 'task_id': task_id})


# Vista completa tarea.
class CompleteTaskView(View):
    def post(self, request, task_id):
        # Marca una tarea como completada y guarda el cambio
        task = get_object_or_404(Task, pk=task_id)
        task.completed = True
        task.save()
        return redirect('list_tasks')


class DeleteTaskView(View):
    def post(self, request, task_id):
        # Elimina una tarea específica y redirige a la lista de tareas
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('list_tasks')
