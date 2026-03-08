from abc import ABC, abstractmethod
class IMediator(ABC):
    @abstractmethod
    def send(self, msg, user, channel_name): pass

class ChatMediator(IMediator): 
    def __init__(self):
        self.channels = {}

    def add_user_to_channel(self, user, channel_name):
        if channel_name not in self.channels:
            self.channels[channel_name] = []
        self.channels[channel_name].append(user)
        print(f"Жүйе: {user.name} '{channel_name}' каналына қосылды") [cite: 190]

    def send(self, msg, sender, channel_name):
        if channel_name not in self.channels: [cite: 215]
            print("Қате: Канал табылмады!")
            return
            
        if sender not in self.channels[channel_name]: [cite: 216]
            print(f"Қате: {sender.name} бұл каналда жоқ!")
            return

        for user in self.channels[channel_name]:
            if user != sender:
                user.receive(msg, sender.name)

class User: 
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    def send(self, msg, channel_name):
        print(f"{self.name} [{channel_name}]-ге жазды: {msg}")
        self.mediator.send(msg, self, channel_name)

    def receive(self, msg, from_user):
        print(f"{self.name} алды ({from_user}-ден): {msg}")

mediator = ChatMediator()
user1 = User(mediator, "Арман")
user2 = User(mediator, "Диана")

mediator.add_user_to_channel(user1, "Python_Group")
mediator.add_user_to_channel(user2, "Python_Group")

user1.send("Сәлем!", "Python_Group")
