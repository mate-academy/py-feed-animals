class Animal:

    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
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
        else:
            return 0


def feed_animals(animals: list):
    return sum([
        animal.appetite for animal in animals
        if animal.is_hungry is True
    ])


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")
