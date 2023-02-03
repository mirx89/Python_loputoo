from tkinter import *
import tkinter.font as tkfont


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model
        self.default_style = tkfont.Font(family="Verdana", size=10)

        # window properties
        self.geometry("1900x1000")
        self.title("Python")
        self.center(self)

        # Create frame
        self.frame_top, self.frame_bottom = self.create_two_frames()
        self.btn_names, self.btn_tasks, self.btn_shuffle, self.btn_save = self.create_all_buttons()
        self.box_names, self.box_tasks, self.box_final = self.create_textboxes()

    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        Netist võetud plokk: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_two_frames(self):
        frame_top = Frame(self, bg="#1E90FF", height=50)
        frame_bottom = Frame(self, bg="#ADFF2F")

        frame_top.pack(fill="both")
        frame_bottom.pack(expand=True, fill="both")

        return frame_top, frame_bottom  # method return two objects

    def create_all_buttons(self):
        btn_names = Button(self.frame_top, text="Names...", font=self.default_style,
                           command=self.controller.click_names)

        btn_tasks = Button(self.frame_top, text="Tasks...", font=self.default_style,
                           command=self.controller.click_tasks)

        btn_final = Button(self.frame_top, text="Shuffle", font=self.default_style,
                           command=self.controller.click_shuffled)

        btn_save = Button(self.frame_top, text="Save...", font=self.default_style,
                          command=self.controller.click_save)

        # Place three buttons and frames
        btn_names.grid(row=0, column=0, padx=20, pady=50, sticky=EW)
        btn_tasks.grid(row=0, column=1, padx=20, pady=50, sticky=EW)
        btn_final.grid(row=0, column=2, padx=20, pady=50, sticky=EW)
        btn_save.grid(row=0, column=3, padx=20, pady=50, sticky=EW)

        return btn_names, btn_tasks, btn_final, btn_save

    def create_textboxes(self):
        box_names = Text(self.frame_bottom, bg='white')
        box_tasks = Text(self.frame_bottom, bg='white')
        box_final = Text(self.frame_bottom, bg='white')

        # Create scrollbar

        box_names.pack(side=LEFT, padx=5, pady=5)
        box_tasks.pack(side=LEFT, padx=5, pady=5)
        box_final.pack(side=LEFT, padx=5, pady=5)
        return box_names, box_tasks, box_final
