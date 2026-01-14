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


def get_task_id():
    task_list = load_tasks()
    if task_list == []:
        return 1
    else:
        pass


def add_task(task_name, task_description):
    task_list = load_tasks()
    task_created_at = utils.get_current_time()
    task_id = get_task_id()
    task_status = "NOT_STARTED"
    task = {"id": task_id, "name": task_name, "description": task_description,
            "status": task_status, "created_at": task_created_at, "last_modified_at": task_created_at}
    task_list.append(task)
    save_tasks(task_list)


def remove_task(task):
    pass
