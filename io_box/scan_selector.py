from tkinter.ttk import OptionMenu, Button
from tkinter import StringVar

class ScanSelector:
    def __init__(self, window):
        self.window = window
        self.options = ["spam", "eggs", "ham"]
        self.selection = StringVar()
        self.dropdown = OptionMenu(self.window, self.selection, *self.options)
        self.delete_button = Button(self.window, text="X", command=self.delete)

    def mount(self):
        self.dropdown.place(x=355, y=150, width=200, height=50)
        self.delete_button.place(x=555, y=150, width=35, height=50)

    def delete(self):
        pass
