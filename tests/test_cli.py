import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_cli.cli import TodoCLI

class TestTodoCLI(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args')
    def test_add_command(self, mock_args, mock_stdout):
        mock_args.return_value = MagicMock(
            command='add',
            description='Новая задача'
        )
        cli = TodoCLI()
        cli.manager.add_task = MagicMock(return_value=MagicMock(
            description='Новая задача',
            id='test-id'
        ))
        cli.save_tasks = MagicMock()
        cli.run()
        output = mock_stdout.getvalue()
        self.assertIn("Задача добавлена: Новая задача (ID: test-id)", output)
