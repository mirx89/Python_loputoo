import random


class Model:

    def __init__(self):
        self.names = []
        self.tasks = []
        self.final = []

    def open_file_names(self, filename):
        self.names = []
        with open(filename, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            for name in all_lines:
                name = name.strip()
                self.names.append(name)
            # print(self.names)  # test

    def open_file_tasks(self, filename):
        self.tasks = []
        with open(filename, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            for task in all_lines:
                task = task.strip()
                self.tasks.append(task)
            # print(self.tasks)  # test

    def shuffle_task(self):
        random.shuffle(self.tasks)
