
# TASK FULL STACK 2024 IBM

## Introduction
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione una lista de tareas pendientes. 

El programa deberá permitir al usuario realizar las siguientes operaciones:
* Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a la lista de tareas pendientes.
* Marcar una tarea como completada: El programa deberá permitir al usuario marcar una tarea como completada, dada su posición en la lista.
* Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas pendientes, numeradas y mostrando su estado (completada o pendiente).
* Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista, dada su posición.

El programa deberá incluir las siguientes características:
* Manejo de excepciones: El programa deberá manejar excepciones en caso de que el usuario ingrese una opción no válida o una posición que no exista en la lista.
* Comentarios explicativos: El código deberá estar comentado para explicar su funcionamiento en cada parte relevante.

## Prerequisites
- Python 3.8 or higher

## Installation

### Clone the Repository
To get started, clone the repository to your local machine:

```
git clone https://github.com/cjosemar/TaskFullStackIbm.git
cd TaskFullStackIbm
```

### Set Up a Virtual Environment
It's recommended to use a virtual environment for Python projects. You can set one up by running:

```python -m venv venv```

Activate the virtual environment:
- On Windows:

```.\venv\Scripts\activate```
- On macOS and Linux:

```source venv/bin/activate```

## Configuration

### Database Setup
This project uses SQLite by default, so no initial setup is required for the database. If you're using a different database, ensure to configure it in the `settings.py` file.

### Perform Database Migrations
Create the necessary database tables:

```python manage.py makemigrations```

```python manage.py migrate```

## Running the Project

To start the development server, run:

```python manage.py runserver```

The application will be available at `http://127.0.0.1:8000/`.
