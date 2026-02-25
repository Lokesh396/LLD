class CPU:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores

    def describe(self):
        # TODO: Print CPU model and core count
        print(f'  CPU: {self.model} ({self.cores} cores)')

class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb

    def describe(self):
        # TODO: Print RAM size
        print(f"  RAM: {self.size_gb} GB")

class HardDrive:
    def __init__(self, capacity_gb):
        self.capacity_gb = capacity_gb

    def describe(self):
        # TODO: Print hard drive capacity
        print(f"  Storage: {self.capacity_gb} GB")

class Computer:
    def __init__(self, name, cpu_model, cpu_cores, ram_gb, storage_gb):
        self.name = name
        # TODO: Create CPU, RAM, and HardDrive internally
        self.cpu = CPU(cpu_model, cpu_cores)
        self.ram = RAM(ram_gb)
        self.hard_drive = HardDrive(storage_gb)

    def describe_specs(self):
        # TODO: Print computer name and describe all components
        print(f'Computer: {self.name}')
        self.cpu.describe()
        self.ram.describe()
        self.hard_drive.describe()

    def upgrade_ram(self, new_size_gb):
        # TODO (Challenge): Replace RAM with a higher-capacity one
        self.ram = RAM(new_size_gb)

import time

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.timestamp = time.time()

    def display(self):
        # TODO: Print message in format "[sender]: text"
        print(f'[{self.sender}]: {self.text}')

class Conversation:
    def __init__(self, title):
        self.title = title
        self.messages = []

    def send_message(self, sender, text):
        # TODO: Create a Message internally and add it to the list
        message = Message(sender, text)
        self.messages.append(message)
    def print_history(self):
        # TODO: Print conversation title and all messages
        print(f'--- {self.title} ---')
        for message in self.messages:
            message.display()

    def delete(self):
        # TODO: Clear all messages (they are destroyed with the conversation)
        self.messages = []

    def get_message_count(self):
        return len(self.messages)

    def forward_message(self, target, message_index):
        # TODO (Challenge): Copy message content into a NEW Message
        # in the target conversation. Don't move the original.
        message = self.messages[message_index:message_index+1]
        target.messages.append(message[0])

if __name__ == "__main__":
    team_chat = Conversation("Team Discussion")
    project_chat = Conversation("Project Alpha")

    team_chat.send_message("Alice", "Hey team, standup in 5 minutes")
    team_chat.send_message("Bob", "Got it, joining now")
    team_chat.send_message("Alice", "Don't forget to update your tasks")

    project_chat.send_message("Charlie", "Deployment is scheduled for Friday")

    print("Before deletion:")
    team_chat.print_history()
    print(f"Project chat has {project_chat.get_message_count()} messages\n")

    # Challenge: forward a message
    team_chat.forward_message(project_chat, 2)
    print("After forwarding:")
    project_chat.print_history()

    # Delete team chat - all its messages are destroyed
    team_chat.delete()
    print("\nAfter deleting team chat:")
    print(f"Team chat has {team_chat.get_message_count()} messages")
    print(f"Project chat still has {project_chat.get_message_count()} messages")

    pc = Computer("Dev Workstation", "Intel i7-13700K", 16, 32, 1000)

    pc.describe_specs()

    # Challenge: upgrade RAM and verify
    pc.upgrade_ram(64)
    print("\nAfter RAM upgrade:")
    pc.describe_specs()

    # When pc is destroyed, all components are destroyed with it.