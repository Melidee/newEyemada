from tkinter.ttk import OptionMenu, Button
from tkinter import StringVar, ttk


class ScanSelector:
    def __init__(self, window, scans):
        self.window = window
        self.scans = scans
        self.options = scans.keys()
        self.selection = StringVar()
        self.dropdown = OptionMenu(self.window, self.selection, command=self.update, *self.options)
        self.delete_button = Button(self.window, text="X", command=self.delete)

    def mount(self):
        self.dropdown.place(x=355, y=150, width=200, height=50)
        self.delete_button.place(x=555, y=150, width=35, height=50)

    def delete(self):
        self.options.pop(self.selection.get())
        self.scans.pop(self.selection.get())

    def update(self):
        pass