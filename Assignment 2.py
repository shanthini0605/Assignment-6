class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def get_info(self):
        print("Coat color:", self.coat_color)
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight
    def bark(self):
        print("Woof!")
    def dig(self):
        print("I'm digging a hole!")
class Bulldog(Dog):
    def __init__(self, name, age, coat_color, height):
        super().__init__(name, age, coat_color)
        self.height = height
    def drool(self):
        print("I'm drooling!")
    def snore(self):
        print("I'm snoring!")
# Create objects
dog1 = Dog("Buddy", 10, "brown")
dog2 = JackRussellTerrier("Max", 5, "white", 15)
dog3 = Bulldog("Rocky", 8, "black", 20)
# Print the description of each dog
dog1.description()
dog2.description()
dog3.description()
# Get the coat color of each dog
dog1.get_info()
dog2.get_info()
dog3.get_info()
# Make the dogs bark
dog2.bark()
dog3.bark()
# Make the dogs dig
dog2.dig()
dog3.dig()
# Make the dogs drool
dog3.drool()
# Make the dogs snore
dog3.snore()