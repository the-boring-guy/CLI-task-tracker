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
    return True


def find_task(task_list, task_id):
    required_task = None
    for task in task_list:
        id_of_task = task.get("id")
        if task_id == id_of_task:
            required_task = task
            return required_task
    return None


def validate_task_id(task_id):
    task_dictionary = load_tasks()
    task_list = list(task_dictionary.get("tasks"))
    return find_task(task_list, task_id) is not None


def remove_task(task_id):
    task_dictionary = load_tasks()
    task_list = list(task_dictionary.get("tasks"))
    required_task = find_task(task_list, task_id)
    if required_task == None:
        return False
    else:
        task_list.remove(required_task)
        task_dictionary.update({"tasks": task_list})
        save_tasks(task_dictionary)
        return True


def update_field(task_id, updation_field, new_value):
    task_dictionary = load_tasks()
    task_list = list(task_dictionary.get("tasks"))
    required_task = find_task(task_list, task_id)
    now = utils.get_current_time()
    if required_task == None:
        return False
    else:
        required_task.update(
            {updation_field: new_value, "last_modified_at": now})
        task_dictionary.update({"tasks": task_list})
        save_tasks(task_dictionary)
        return True


def list_tasks():
    task_dictionary = load_tasks()
    task_list = list(task_dictionary.get("tasks"))
    return task_list


def filter_by_status(task_status):
    task_dictionary = load_tasks()
    task_list = task_dictionary.get("tasks")
    filtered_tasks = [task for task in task_list if task.get(
        "status") == task_status]
    return filtered_tasks
