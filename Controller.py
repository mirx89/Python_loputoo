from tkinter import filedialog, INSERT, messagebox
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
        self.view.box_names.delete("1.0", "end")
        txt_names = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        # print(txt_names)  # test
        if txt_names != "":
            messagebox.showerror("Viga", "Valitud fail on tühi.")
            self.model.open_file_names(txt_names)
            if len(self.model.names) > 0:
                for name in self.model.names:
                    self.view.box_names.insert(INSERT, name + "\n")
                # print(self.model.names) #  test

    def click_tasks(self):
        self.view.box_tasks.delete("1.0", "end")
        txt_tasks = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        # print(tasks)  # test
        if txt_tasks != "":
            messagebox.showerror("Viga", "Valitud fail on tühi.")
            self.model.open_file_tasks(txt_tasks)
            if len(self.model.tasks) > 0:
                for task in self.model.tasks:
                    self.view.box_tasks.insert(INSERT, task + "\n")

    def click_shuffled(self):
        if len(self.model.names) > len(self.model.tasks):
            messagebox.showerror("Viga", "Ülesannete arv on liiga väike.")
        else:
            self.view.box_final.delete("1.0", "end")
            self.model.shuffle_task()
            x = 0
            for name in self.model.names:
                self.view.box_final.insert(INSERT, name + " - " + self.model.tasks[x] + "\n")
                self.model.final.append(name + " - " + self.model.tasks[x])
                x += 1

    def click_save(self):
        if len(self.model.final) != 0:
            final = filedialog.asksaveasfilename(
                filetypes=[("txt file", ".txt")],
                defaultextension=".txt",
                initialdir='D:\\my_data\\my_html\\')
            print(final)
            if final != "":
                """ File exists"""
                with open(final, "a", encoding="utf-8") as f:
                    for save in self.model.final:
                        f.write(save + "\n")

        # TODO enne salvestamist kontrollida kas 3. listis on midagi enne kui salvestada saab
