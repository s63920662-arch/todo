import json
import os
from .core import Task
from .errors import StorageError

class JSONStorage:
    def __init__(self, filepath='tasks.json'):
        self.filepath = filepath

    def load_tasks(self):
        try:
            if not os.path.exists(self.filepath):
                return []
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(task_data) for task_data in data]
        except (json.JSONDecodeError, IOError) as e:
            raise StorageError(f"Ошибка загрузки данных: {e}")

    def save_tasks(self, tasks):
        try:
            data = [task.to_dict() for task in tasks]
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            raise StorageError(f"Ошибка сохранения данных: {e}")
