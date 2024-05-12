from django.db import models


# Definimos el modelo de la tarea
class Task(models.Model):
    # Almacena la descripción de la tarea.
    description = models.CharField(max_length=255)
    # Inndica si la tarea ha sido completada o no.
    completed = models.BooleanField(default=False)

    # Devolvemos la descripción de la tarea y su estado ("Completed" o "Pending").
    def __str__(self):
        return f"{self.description} ({'Completed' if self.completed else 'Pending'})"
