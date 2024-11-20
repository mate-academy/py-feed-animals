class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if not self.is_hungry:
            return 0
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = not self.is_hungry
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str, appetite: int = 3, is_hungry: bool = True):
        super(Cat, self).__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, appetite: int = 7, is_hungry: bool = True):
        super(Dog, self).__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list):
    return sum(animal.feed() for animal in animals)
