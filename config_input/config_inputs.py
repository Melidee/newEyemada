from .target_input import TargetInput
from .port_input import PortInput
from .name_input import NameInput


class ConfigInputs:
    def __init__(self, window):
        self.window = window
        self.target_input = TargetInput(window)
        self.port_input = PortInput(window)
        self.name_input = NameInput(window)

    def mount(self):
        self.target_input.mount()
        self.port_input.mount()
        self.name_input.mount()

    def get(self):
        return self.name_input.get(), self.target_input.get(), self.port_input.get()
