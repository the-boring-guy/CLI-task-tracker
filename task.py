import json


class Task:
    def __init__(self, id, name, description, status, created_at, last_modified_at):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at
        self.last_modified_at = last_modified_at
