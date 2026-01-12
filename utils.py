import datetime
import json


def get_current_time():
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S on %d-%m-%Y")
