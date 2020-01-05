import tkinter as tk


class FretboardOrientationSelectFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.description_label = tk.Label(self, text='Orientation')
        self.description_label.pack()
        self.selection_frame = tk.Frame(self)
        self.orientation = tk.StringVar()
        self.orientation.set(None)
        for orientation in ['Vertical', 'Horizontal']:
            b = tk.Radiobutton(self.selection_frame, text=orientation,
                               variable=self.orientation, value=orientation[0])
            b.config(indicatoron=0)
            b.pack(side=tk.LEFT)
        self.orientation.set('V')
        self.selection_frame.pack()
        self.selection_frame.config(borderwidth=1)
        self.config(borderwidth=2, relief=tk.GROOVE)
        self.pack()

    def get_orientation(self):
        return self.orientation.get()
