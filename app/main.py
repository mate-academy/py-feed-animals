class Animal:
    def __init__(
            self,
            name: str,
            appetite: int = 0,
            is_hungry: bool = True
    ):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        print(f"Eating {self.appetite} food points...")
        if self.is_hungry:
            self.is_hungry = False
            result = self.appetite
            self.appetite = 0
            return result
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(animals: list):
    return sum(animal.appetite for animal in animals if animal.is_hungry)
