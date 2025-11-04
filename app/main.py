class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetit = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetit} food points...")
            self.is_hungry = False
            return self.appetit
        return 0

class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")

def feed_animals(animals):
    total = 0
    for animal in animals:
        total += animal.feed()
    return total
