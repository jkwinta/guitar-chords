import tkinter as tk

from guitar_chords import tunings


# TODO

class SelectTuningFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_label = tk.Label(self, text='Tuning')
        self.frame_label.pack()
        self.tuning_menu_button = tk.Menubutton(self)
        # self.tuning_menu_button.pack()
        self.tuning_menu_button.menu = tk.Menu(self.tuning_menu_button,
                                               tearoff=0)
        self.tuning_menu_button['menu'] = self.tuning_menu_button.menu

        self.text_display_variable = tk.StringVar()
        self.tuning_menu_button.config(textvariable=self.text_display_variable)

        for tuning_name in tunings:
            self.tuning_menu_button.menu.add_command(
                label=tuning_name,
                command=lambda s=tuning_name: self.text_display_variable.set(s))

        # self.tuning_menu_button.menu.add_checkbutton(
        #     label='asdf',
        #     command=lambda: self.text_display_variable.set('asdf'))
        # self.tuning_menu_button.menu.add_checkbutton(
        #     label='qwer',
        #     command=lambda: self.text_display_variable.set('qwer'))

        self.tuning_menu_button.pack(fill=tk.X)
        # self.tuning_menu_button.config(width=20)

        self.pack(fill=tk.X)
        self.config(borderwidth=2, relief=tk.GROOVE)

# https://www.tutorialspoint.com/python/tk_menubutton.htm
