import utils
import storage


VALID_COMMANDS = ('add', 'remove', 'update', 'list', 'filter')
VALID_STATUS = ('NOT STARTED', 'ONGOING', 'COMPLETED')


def show_menu():
    print('----------------Menu-----------------')
    print('1. "add"- to add tasks')
    print('2. "remove"- to remove tasks')
    print('3. "update"- to update tasks')
    print('4. "list"- to see all tasks in list form')
    print('5. "filter"- to filter tasks by status')


def get_command():
    while True:
        command = input(
            "Enter a menu option to continue(q to quit): ").strip().lower()
        if command == 'q':
            return command
        elif command not in VALID_COMMANDS:
            print("INVALID COMMAND!!!! PLEASE TRY AGAIN....")
        else:
            return command


def get_task_id():
    while True:
        task_id = input("Enter the task id(q to quit): ").strip().lower()
        if task_id == 'q':
            return task_id
        elif utils.check_natural_number(task_id) is False:
            print("INVALID INPUT!!!! TASK ID MUST BE A NATURAL NUMBER....")
        else:
            if storage.validate_task_id(task_id):
                return task_id
            else:
                print("INVALID INPUT!!!! TASK LINKED TO THIS ID DOES NOT EXIST....")


def show_task_list():
    print('-------------Task List---------------')
    task_list = storage.list_tasks()
    if task_list == []:
        print("NO TASKS FOUND!!!! PLEASE ADD TASKS TO VIEW....")
    else:
        for task in task_list:
            utils.print_task(task)


def get_input_add_task():
    task_name = utils.get_user_input("task name")
    task_description = utils.get_user_input("task description")
    return task_name, task_description


def add_task():
    task_name, task_description = get_input_add_task()
    storage.add_task(task_name, task_description)


def remove_task():
    task_id = get_task_id()
    storage.remove_task(task_id)


def get_valid_status():
    while True:
        task_status = input("Enter task status(q to quit): ").strip().upper()
        if task_status in VALID_STATUS:
            return task_status
        elif task_status.lower() == 'q':
            return task_status
        else:
            print("INVALID STATUS!!!! PLEASE ENTER VALID STATUS....")


def filter_tasks():
    task_status = get_valid_status()
    filtered_tasks = storage.filter_by_status(task_status)
    if filtered_tasks == []:
        print(
            f"NO TASKS MARKED AS '{task_status}' FOUND!!!! PLEASE TRY AGAIN OR VIEW ALL TASKS LIST....")
    else:
        for task in filtered_tasks:
            utils.print_task(task)


def main():
    print('---------------Welcome---------------')
    print('-------------------------------------')
    show_menu()
    user_command = get_command()


if __name__ == "__main__":
    get_valid_status()
