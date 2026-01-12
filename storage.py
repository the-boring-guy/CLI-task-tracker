import json


STORAGE_FILE = "storage.json"


def load_tasks():
    try:
        with open(STORAGE_FILE, 'r') as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def add_task():
    pass


def remove_task():
    pass


def save_tasks():
    pass
