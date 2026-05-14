import argparse
from .core import TaskManager
from .storage import JSONStorage

class TodoCLI:
    def __init__(self):
        self.manager = TaskManager()
        self.storage = JSONStorage()
        self.load_tasks()

    def load_tasks(self):
        try:
            tasks = self.storage.load_tasks()
            self.manager.tasks = tasks
        except Exception as e:
            print(f"Предупреждение: не удалось загрузить задачи: {e}")

    def save_tasks(self):
        try:
            self.storage.save_tasks(self.manager.tasks)
        except Exception as e:
            print(f"Ошибка: не удалось сохранить задачи: {e}")
            raise

    def run(self):
        parser = argparse.ArgumentParser(description='Todo CLI — управление списком дел')
        subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

        # Команда add
        add_parser = subparsers.add_parser('add', help='Добавить задачу')
        add_parser.add_argument('description', help='Описание задачи')

        # Команда list
        list_parser = subparsers.add_parser('list', help='Показать все задачи')

        # Команда complete
        complete_parser = subparsers.add_parser('complete', help='Отметить задачу как выполненную')
        complete_parser.add_argument('task_id', help='ID задачи')

        # Команда delete
        delete_parser = subparsers.add_parser('delete', help='Удалить задачу')
        delete_parser.add_argument('task_id', help='ID задачи')

        args = parser.parse_args()

        if args.command == 'add':
            task = self.manager.add_task(args.description)
            self.save_tasks()
            print(f"Задача добавлена: {task.description} (ID: {task.id})")

        elif args.command == 'list':
            tasks = self.manager.list_tasks()
            if not tasks:
                print("Список задач пуст")
            else:
                for task in tasks:
                    status = "✓" if task.completed else "○"
                    print(f"{status} {task.description} (ID: {task.id})")

        elif args.command == 'complete':
            if self.manager.complete_task(args.task_id):
                self.save_tasks()
                print(f"Задача {args.task_id} отмечена как выполненная")
            else:
                print(f"Ошибка: задача {args.task_id} не найдена")

        elif args.command == 'delete':
            if self.manager.delete_task(args.task_id):
                self.save_tasks()
                print(f"Задача {args.task_id} удалена")
            else:
                print(f"Ошибка: задача {args.task_id} не найдена")

        else:
            parser.print_help()
