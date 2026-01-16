import utils
import storage


VALID_COMMANDS = ('add', 'remove', 'update', 'list', 'filter')


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


def main():
    print('---------------Welcome---------------')
    print('-------------------------------------')
    show_menu()
    get_command()


if __name__ == "__main__":
    main()
