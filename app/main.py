class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        result = 0
        if self.is_hungry:
            result = self.appetite
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = False
        return result


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


def feed_animals(ls: list):
    return sum(animal.appetite for animal in ls if animal.is_hungry)
