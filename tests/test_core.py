import unittest
import sys
import os

# Добавляем путь к корневому каталогу проекта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_cli.core import Task, TaskManager, ValidationError

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Купить молоко")
        self.assertEqual(task.description, "Купить молоко")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.id)

    def test_empty_description_raises_error(self):
        with self.assertRaises(ValidationError):
            Task("")

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Новая задача")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0], task)
