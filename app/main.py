class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            food_points = self.appetite
            self.is_hungry = False
            return food_points
        return 0


class Cat(Animal):
    def __init__(self, name, appetite=3, is_hungry=True):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, appetite=7, is_hungry=True):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(animals: list):
    result = 0
    for animal in animals:
        result += Animal.feed(animal)
    return result
