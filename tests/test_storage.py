import unittest
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_cli.storage import JSONStorage
from todo_cli.core import Task
from todo_cli.errors import StorageError

class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        self.storage = JSONStorage(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_tasks(self):
        task1 = Task("Задача 1")
        task2 = Task("Задача 2", completed=True)
        self.storage.save_tasks([task1, task2])
        loaded_tasks = self.storage.load_tasks()
        self.assertEqual(len(loaded_tasks), 2)
