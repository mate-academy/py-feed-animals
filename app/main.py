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
            self.is_hungry = False
            return self.appetite
        return 0


def feed_animals(animal: list):
    return sum(member.feed() for member in animal)


class Cat(Animal):

    def __init__(self, name, appetite: int = 3, is_hungry=True):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name, appetite: int = 7, is_hungry=True):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")
