class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0

class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")
        # Let's set the cat to be hungry after catching a mouse, implying it gets an appetite.
        self.is_hungry = True

class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")
        # Let's make the dog less hungry after delivering slippers, simulating the reward.
        if self.is_hungry:
            self.is_hungry = False  # Dog isn't hungry anymore after delivering slippers.

def feed_animals(animals):
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food
