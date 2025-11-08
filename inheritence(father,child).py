class dad:
    def __init__(self, eyes, aggresive):
        self.eyes = eyes
        self.aggresive = aggresive
    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggresive", self.aggresive)
class son(dad):
    def __init__(self, name, age, eyes, aggresive):
        self.name = name
        self.age = age

        super().__init__(eyes, aggresive)

obj = son("Penguin", 8, "blue", True)

obj.display()
print("Your name is", obj.name)
print("Your age is", obj.age)
        