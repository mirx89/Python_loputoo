from tkinter import filedialog

from Model import Model
from View import View


class Controller:

    def __init__(self, db_name=None):
        self.model = Model()
        if db_name is not None:
            self.model.database_name = db_name  # database file changed
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_names(self):
        names = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        print(names)

    def click_tasks(self):
        names = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        print(names)

    def click_shuffled(self):
        pass

    def click_save(self):
        file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt",
            initialdir='D:\\my_data\\my_html\\')
        print(file)
