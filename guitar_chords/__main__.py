import tkinter as tk
from guitar_chords.gui import MainWindow

root = tk.Tk()
app = MainWindow(root)
root.wm_title('Guitar chords')
root.mainloop()
