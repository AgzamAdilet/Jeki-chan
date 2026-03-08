from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): pass
    @abstractmethod
    def undo(self): pass

class Light:
    def on(self): print("Жарық қосылды")
    def off(self): print("Жарық өшірілді")

class Thermostat:
    def __init__(self): self.temp = 20
    def set_temp(self, val):
        self.temp = val
        print(f"Температура орнатылды: {self.temp}°C")

class LightOnCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.on()
    def undo(self): self.light.off()

class TempCommand(Command):
    def __init__(self, thermo, new_temp):
        self.thermo = thermo
        self.prev_temp = thermo.temp
        self.new_temp = new_temp
    def execute(self): self.thermo.set_temp(self.new_temp)
    def undo(self): self.thermo.set_temp(self.prev_temp)

class RemoteControl:
    def __init__(self): self.history = []
    def press_button(self, command):
        command.execute()
        self.history.append(command)
    def undo_button(self):
        if self.history:
            self.history.pop().undo()
        else: print("Болдырмау үшін команда жоқ")
light = Light()
remote = RemoteControl()
on_cmd = LightOnCommand(light)

remote.press_button(on_cmd)  # Қосу
remote.undo_button()         # Болдырмау (өшіру)