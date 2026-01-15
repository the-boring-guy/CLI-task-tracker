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
    command = input(
        "Enter a menu option to continue(q to quit): ").strip().lower()
    if command in VALID_COMMANDS:
        return command
    else:
        print("Not a valid command!!!!Please try again....")
        command = input(
            "Enter a menu option to continue(q to quit): ").strip().lower()


def main():
    print('---------------Welcome---------------')
    print('-------------------------------------')
    show_menu()


if __name__ == "__main__":
    main()
