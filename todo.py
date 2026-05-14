#!/usr/bin/env python
"""
Скрипт для запуска Todo CLI
"""
from todo_cli.cli import TodoCLI

if __name__ == '__main__':
    cli = TodoCLI()
    cli.run()


