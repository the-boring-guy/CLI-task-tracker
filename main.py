import utils
import storage


VALID_COMMANDS = ('menu', 'add', 'remove', 'update',
                  'list', 'filter', 'change')
VALID_STATUS = ('NOT STARTED', 'ONGOING', 'COMPLETED')


def show_menu():
    print('----------------Menu-----------------')
    print('1. "menu"- to show main menu')
    print('2. "add"- to add tasks')
    print('3. "remove"- to remove tasks')
    print('4. "update"- to update task status')
    print('5. "list"- to see all tasks in list form')
    print('6. "filter"- to filter tasks by status')
    print('7. "change"- to change task particulars like name or description')


def get_command():
    while True:
        command = input(
            "Enter a menu option to continue(q to quit): ").strip().lower()
        if command == 'q':
            return command
        elif command not in VALID_COMMANDS:
            print(
                "INVALID COMMAND!!!! PLEASE ENTER VALID COMMANDS FROM THE ONES SHOWN BELOW....")
            for command in VALID_COMMANDS:
                print(command)
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
    if task_name or task_description is 'q':
        return False
    else:
        storage.add_task(task_name, task_description)


def remove_task():
    task_id = get_task_id()
    if task_id is 'q':
        return False
    else:
        storage.remove_task(task_id)


def get_valid_status():
    while True:
        task_status = input("Enter task status(q to quit): ").strip().upper()
        if task_status in VALID_STATUS:
            return task_status
        elif task_status.lower() == 'q':
            return task_status
        else:
            print(
                "INVALID STATUS!!!! PLEASE ENTER VALID STATUS OUT OF THE ONES SHOWN BELOW....")
            for status in VALID_STATUS:
                print(status)


def filter_tasks():
    task_status = get_valid_status()
    if task_status is 'q':
        return False
    else:
        filtered_tasks = storage.filter_by_status(task_status)
        if filtered_tasks == []:
            print(
                f"NO TASKS MARKED AS '{task_status}' FOUND!!!! PLEASE TRY AGAIN OR VIEW ALL TASKS LIST....")
        else:
            for task in filtered_tasks:
                utils.print_task(task)


def get_input_update_field():
    task_field = utils.get_user_input("field to be updated")
    new_value = utils.get_user_input("new value of selected field")
    return task_field, new_value


def update_status():
    task_id = get_task_id()
    new_status = get_valid_status()
    if task_id or new_status is 'q':
        return False
    else:
        storage.update_field(task_id, "status", new_status)


def update_other_field():
    task_id = get_task_id()
    updation_field, new_value = get_input_update_field()
    if task_id or updation_field is 'q':
        return False
    else:
        storage.update_field(task_id, updation_field, new_value)


def main():
    is_running = True
    print('---------------Welcome---------------')
    print('-------------------------------------')
    show_menu()
    while is_running:
        user_command = get_command()
        if user_command is 'q':
            is_running = False
        else:
            match user_command:
                case 'add':
                    continue_running = add_task()
                    if continue_running is False:
                        is_running = False
                case 'remove':
                    continue_running = remove_task()
                    if continue_running is False:
                        is_running = False
                case 'list':
                    show_task_list()
                case 'filter':
                    continue_running = filter_tasks()
                    if continue_running is False:
                        is_running = False
                case 'update':
                    continue_running = update_status()
                    if continue_running is False:
                        is_running = False
                case 'menu':
                    show_menu()
                case 'change':
                    continue_running = update_other_field()
                    if continue_running is False:
                        is_running = False


if __name__ == "__main__":
    main()
