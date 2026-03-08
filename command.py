from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self): pass
    @abstractmethod
    def undo(self): pass

class TV:
    def on(self): print("Теледидар қосылды")
    def off(self): print("Теледидар өшірілді")

class AirConditioner:
    def set_temp(self, t): print(f"Кондиционер температурасы: {t}°C")

class TVOnCommand(ICommand):
    def __init__(self, tv): self.tv = tv
    def execute(self): self.tv.on()
    def undo(self): self.tv.off()

class MacroCommand(ICommand):
    def __init__(self, commands): self.commands = commands
    def execute(self): 
        for cmd in self.commands: cmd.execute()
    def undo(self): 
        for cmd in reversed(self.commands): cmd.undo()

class RemoteControl:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def press_button(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo()
            self.redo_stack.append(cmd)
        else: print("Болдырмауға әрекет жоқ") [cite: 144]

    def redo(self):
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.execute()
            self.undo_stack.append(cmd)
