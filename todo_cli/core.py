import uuid
from datetime import datetime
from .errors import ValidationError

class Task:
    def __init__(self, description, task_id=None, completed=False):
        if not description or not description.strip():
            raise ValidationError("Описание задачи не может быть пустым")
        self.id = task_id or str(uuid.uuid4())
        self.description = description.strip()
        self.completed = completed
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            description=data['description'],
            task_id=data['id'],
            completed=data['completed']
        )
        task.created_at = datetime.fromisoformat(data['created_at'])
        return task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        return task

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return True
        return False

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self):
        return self.tasks
