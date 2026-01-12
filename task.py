import json


class Task:
    def __init__(self, id, description, status, created_at, last_modified_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.last_modified_at = last_modified_at

    def mark_not_done():
        pass

    def mark_done():
        pass

    def mark_in_transit():
        pass

    def last_modified_log():
        pass
