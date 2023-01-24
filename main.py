from tkinter import Tk


class MainWindow:
    def __init__(self) -> None:
        self.window = Tk()
        self.setup_window()

    def setup_window(self):
        self.window.geometry("600x600")
        self.window.title("Eyemada")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    win = MainWindow()
    win.run()
