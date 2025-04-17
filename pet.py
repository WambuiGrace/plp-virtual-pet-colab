class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
	print(f"Creating pet: {self.name}")

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy > 0:
            print(f"{self.name} is playing...")
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        if self.energy > 2:
            print(f"{self.name} is training...")
            self.energy -= 3
            self.tricks.append(trick)
            print(f"{self.name} learned how to {trick}!")
        else:
            print(f"{self.name} is too tired to train!")

    def show_tricks(self):
        print(f"{self.name}'s tricks: {', '.join(self.tricks) if self.tricks else 'No tricks yet.'}")

    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")