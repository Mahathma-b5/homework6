from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base for all commands."""
    
    @abstractmethod
    def execute(self, *args):
        """Execute the command with the provided arguments."""
        pass

class CommandHandler:
    """Handles registration and execution of commands."""
    
    def __init__(self):
        self.commands = {}
    
    def Register_Command(self, command_name: str, command: Command):
        """Register a command under the given name."""
        self.commands[command_name] = command
        print(f"Registered command: {command_name}")
    
    def Execute_Command(self, command_name: str, *args):
        """Execute a command by name if it is registered; otherwise, print an error message."""
        try:
            if command_name in self.commands:
                self.commands[command_name].execute(*args)
            else:
                print(f"{command_name} :Command not found")
        except (KeyError, TypeError):
            print(f"{command_name} : There is no such command or invalid arguments for the command are given")
    
    def Get_Registered_Commands(self):
        """Return a list of all registered command names."""
        return list(self.commands.keys())
