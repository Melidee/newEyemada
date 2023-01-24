from .target_input import TargetInput
from .port_input import PortInput


class ConfigInputs:
    def __init__(self, window):
        self.window = window
        self.target_input = TargetInput(window)
        self.port_input = PortInput(window)

    def mount(self):
        self.target_input.mount()
        self.port_input.mount()

    def get(self):
        return self.target_input.get(), self.port_input.get()
