from tkinter import *
import tkinter.font as tkfont


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model

        self.default_style = tkfont.Font(family="Verdana", size=10)

        # window properties
        self.geometry("450x600")
        self.title("Python")
        self.center(self)

        # Create frame
        self.frame_top, self.frame_bottom = self.create_two_frames()
        self.btn_names, self.btn_tasks, self.btn_shuffle, self.btn_save = self.create_all_buttons()
        self.lbl_resultr = self.create_all_labels()

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
        btn_names = Button(self.frame_top, text="Names...", font=self.default_style, command=self.controller.click_names)

        btn_tasks = Button(self.frame_top, text="Tasks...", font=self.default_style, command=self.controller.click_tasks)

        btn_shuffled = Button(self.frame_top, text="Shuffle", font=self.default_style, command=self.controller.click_shuffled)

        btn_save = Button(self.frame_top, text="Save", font=self.default_style,
                          command=self.controller.click_save)

        # Place three buttons and frames
        btn_names.grid(row=0, column=0, padx=20, pady=50, sticky=EW)
        btn_tasks.grid(row=0, column=1, padx=20, pady=50, sticky=EW)
        btn_shuffled.grid(row=0, column=2, padx=20, pady=50, sticky=EW)
        btn_save.grid(row=0, column=3, padx=20, pady=50, sticky=EW)

        return btn_names, btn_tasks, btn_shuffled, btn_save

    def create_all_labels(self):

        lbl_names = Label(self.frame_bottom, text="Names", anchor="w", font=self.default_style)
        lbl_tasks = Label(self.frame_bottom, text="Tasks", anchor="center", font=self.default_style)
        lbl_shuffled = Label(self.frame_bottom, text="Shuffled", anchor="e", font=self.default_style)

        lbl_names.grid(row=1, column=0, padx=30, pady=2)
        lbl_tasks.grid(row=1, column=1, padx=30, pady=2)
        lbl_shuffled.grid(row=1, column=2, padx=30, pady=2)

        name_image = Frame(self.frame_bottom, bg="white", width=130, height=330)
        name_image.grid(row=2, column=0, rowspan=4, padx=5, pady=5)
        tasks_image = Frame(self.frame_bottom, bg="white", width=130, height=330)
        tasks_image.grid(row=2, column=1, rowspan=4, padx=5, pady=5)
        shuffled_image = Frame(self.frame_bottom, bg="white", width=130, height=330)
        shuffled_image.grid(row=2, column=2, rowspan=4, padx=5, pady=5)

        # Txtbox

        """scrolled tekst kastide asemel"""
