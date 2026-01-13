import json
import utils


STORAGE_FILE = "storage.json"


def load_tasks():
    try:
        with open(STORAGE_FILE, 'r') as file:
            task_list = json.load(file)
            return task_list
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(task_list):
    with open(STORAGE_FILE, 'w') as file:
        json.dump(task_list, file)


def add_task(task):
    pass


def remove_task(task):
    pass
