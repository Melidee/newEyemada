from tkinter import Tk
from config_input.config_inputs import ConfigInputs
from io_box.io_box import IOBox


class MainWindow:
    def __init__(self) -> None:
        self.window = Tk()
        self.setup_window()

        self.inputs = ConfigInputs(self.window)
        self.io_box = IOBox(self.window)
        self.mount_components()

    def setup_window(self):
        self.window.geometry("600x600")
        self.window.title("Eyemada")

    def mount_components(self):
        self.inputs.mount()
        self.io_box.mount()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    win = MainWindow()
    win.run()
