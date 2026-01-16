import datetime


def get_current_time():
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S on %d-%m-%Y")
    return now


def check_natural_number(num):
    try:
        num = int(num)
        if num <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


def print_task(task):
    print(f"Task id = {task.get('id')}")
    print(f"Task name = {task.get('name')}")
    print(f"Task status = {task.get('status')}")
    print(f"Task description = {task.get('description')}")
    print(f"Task created at = {task.get('created_at')}")
    print(f"Last modified at = {task.get('last_modified_at')}")
    print('**********************')


def get_user_input(what):
    while True:
        user_input = input(f"Enter {what}(q to quit): ").strip()
        if user_input == '':
            print("INVALID INPUT!!!! INPUT CANNOT BE EMPTY....")
        else:
            return user_input
