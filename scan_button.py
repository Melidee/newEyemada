from tkinter.ttk import Button


class ScanButton:
    def __init__(self, window, scan_func):
        self.window = window
        self.button = Button(self.window, text="Scan", command=scan_func)

    def mount(self):
        self.button.place(x=500, y=30, width=80, height=80)