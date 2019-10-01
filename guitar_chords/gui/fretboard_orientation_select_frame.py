import tkinter as tk


class FretboardOrientationSelectFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.description_label = tk.Label(self, text='Orientation')
        self.description_label.pack()
        self.selection_frame = tk.Frame(self)
        self.orientation = tk.StringVar()
        self.orientation = tk.BooleanVar()
        self.orientation.set(False)
        # for text, value in [('Vertical', 'scale'), ('Chords', 'chord')]:
        for value, text in enumerate(['Vertical', 'Horizontal']):
            b = tk.Radiobutton(self.selection_frame, text=text,
                               variable=self.orientation, value=bool(value))
            b.config(indicatoron=0)
            b.pack(side=tk.LEFT)
        self.selection_frame.pack()
        self.selection_frame.config(borderwidth=1)
        self.config(borderwidth=2, relief=tk.GROOVE)
        self.pack()

    def get_orientation(self):
        return ['Vertical', 'Horizontal'][self.orientation.get()]
