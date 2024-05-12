from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def test_task_creation(self):
        """ Prueba la creación de una nueva tarea y verifica que se guarde correctamente. """
        task = Task.objects.create(description="Test task", completed=False)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)


class TaskViewsTests(TestCase):
    def test_home_page_status_code(self):
        """ Prueba que la página principal se cargue correctamente. """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task_view(self):
        """ Prueba la funcionalidad de añadir una tarea mediante el formulario. """
        response = self.client.post('/add/', {'description': 'Test new task', 'completed': False})
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().description, 'Test new task')

    def test_task_detail_view(self):
        """ Prueba que la vista de detalles de la tarea muestre la tarea correcta. """
        task = Task.objects.create(description="Detail view task", completed=False)
        url = reverse('task_detail', args=[task.id])
        response = self.client.get(url)
        self.assertContains(response, "Detail view task")
