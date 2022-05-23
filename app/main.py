class Animal:

    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            points = self.appetite
            self.appetite = 0
            return points


class Cat(Animal):

    def __init__(self, name: str, appetite: int = 3, is_hungry: bool = True):
        super(Cat, self).__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, appetite: int = 7, is_hungry: bool = True):
        super(Dog, self).__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(animals):
    return sum([animal.appetite for animal in animals
                if animal.is_hungry is True])
