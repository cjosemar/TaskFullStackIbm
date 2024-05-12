from django import forms

from Task.models import Task


# Formulario para añadir/editar tareas
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'completed']
