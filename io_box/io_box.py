from tkinter import Text
from .scan_selector import ScanSelector


class IOBox:
    def __init__(self, window):
        self.window = window
        self.scan_selector = ScanSelector(self.window, self)
        self.text_box = Text(self.window)
        self.text_box.place(x=10, y=200, width=580, height=390)
