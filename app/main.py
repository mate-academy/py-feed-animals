class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name, is_hungry=True, appetite=3):
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        self.is_hungry = False
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry=True, appetite=7):
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        self.is_hungry = False
        print("The slippers delivered!")


def feed_animals(animals):
    result = 0
    for animal in animals:
        if animal.is_hungry:
            result += animal.appetite
            animal.is_hungry = False
    return result
