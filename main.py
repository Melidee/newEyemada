from tkinter import Tk
from config_input import config_inputs


class MainWindow:
    def __init__(self) -> None:
        self.window = Tk()

        self.inputs = config_inputs.ConfigInputs(self.window)
        self.inputs.mount()

        self.setup_window()

    def setup_window(self):
        self.window.geometry("600x600")
        self.window.title("Eyemada")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    win = MainWindow()
    win.run()
