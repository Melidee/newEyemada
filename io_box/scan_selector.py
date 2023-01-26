from tkinter.ttk import OptionMenu, Button
from tkinter import StringVar, ttk


class ScanSelector:
    def __init__(self, window, io_box):
        self.window = window
        self.io_box = io_box
        self.scans = {"Google & Cloudflare DNS":""}
        self.options = self.scans.keys()
        self.selection = StringVar()
        self.dropdown = self.make_dropdown()
        self.delete_button = Button(self.window, text="X", command=self.delete)
        self.mount_dropdown()
        self.mount_delete_button()

    def mount_dropdown(self):
        self.dropdown.place(x=355, y=150, width=200, height=50)

    def mount_delete_button(self):
        self.delete_button.place(x=555, y=150, width=35, height=50)

    def delete(self):
        self.scans.pop(self.selection.get())
        self.update_options()

    def add_scan(self, scan_name, scan_output):
        self.scans[scan_name] = scan_output
        self.update_options()

    def update_frame(self):
        return self.scans[self.selection.get()]

    def make_dropdown(self):
        return OptionMenu(self.window, self.selection, command=self.update_frame, *self.options)

    def update_options(self):
        self.options = self.scans.keys()
        self.dropdown.destroy()
        self.dropdown = self.make_dropdown()
        self.mount_dropdown()
