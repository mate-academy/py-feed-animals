class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
    
    def print_name(self):
        print(f"Hello, I'm {self.name}.")
    
    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points . . .")
            self.is_hungry = False
            return self.appetite
        else:
            return 0

class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(name, appetite=3, is_hungry=is_hungry)
    
    @staticmethod
    def catch_mouse():
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(name, appetite=7, is_hungry=is_hungry)
    
    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")

def feed_animals(animals: list) -> int:
    points = 0
    for animal in animals:
        points += animal.appetite
        Animal.feed(animal)
    return points