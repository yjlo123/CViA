__author__ = 'siwei'

class BaseConverter:
    def __init__(self):
        self.type = "-"

    def set_path(self, file_name):
        self.path = file_name
        self.text = file_name + "\n"

    def get_type(self):
        return self.type