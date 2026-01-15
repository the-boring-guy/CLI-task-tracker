import json
import utils


STORAGE_FILE = "storage.json"


def load_tasks():
    try:
        with open(STORAGE_FILE, 'r') as file:
            task_dictionary = json.load(file)
            return dict(task_dictionary)
    except FileNotFoundError:
        return {"last_id": 0, "tasks": []}
    except json.JSONDecodeError:
        return {"last_id": 0, "tasks": []}


def save_tasks(task_dictionary):
    with open(STORAGE_FILE, 'w') as file:
        json.dump(task_dictionary, file)


def add_task(task_name, task_description):
    task_dictionary = load_tasks()
    task_list = list(task_dictionary.get("tasks"))
    last_id = task_dictionary.get("last_id")
    task_created_at = utils.get_current_time()
    task_id = last_id + 1
    task_status = "NOT_STARTED"
    task = {"id": task_id, "name": task_name, "description": task_description,
            "status": task_status, "created_at": task_created_at, "last_modified_at": task_created_at}
    task_list.append(task)
    task_dictionary.update({"tasks": task_list})
    last_id += 1
    task_dictionary.update({"last_id": last_id})
    save_tasks(task_dictionary)


def remove_task(task_id):
    pass
