from tkinter.ttk import Label, Entry
from tkinter import StringVar

class PortInput:
    def __init__(self, window):
        self.window = window
        self.user_input = StringVar()
        self.entryLabel = Label(self.window, text="Ports")
        self.entry = Entry(self.window, textvariable=self.user_input)

    def mount(self):
        self.entryLabel.place(x=20, y=70, height=30, width=250)
        self.entry.place(x=20, y=100, height=30, width=250)

    def get(self):
        return self.user_input.get()
