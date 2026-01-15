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
