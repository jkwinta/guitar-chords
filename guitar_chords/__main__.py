import tkinter as tk
from .gui import MainWindow

root = tk.Tk()
app = MainWindow(root)
root.wm_title('Guitar chords')
root.mainloop()
