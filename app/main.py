class Animal:

    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry is True:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        self.appetite = 0
        return self.appetite


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3)
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7)
        self.is_hungry = is_hungry

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    total = 0
    for animal in animals:
        animal.feed()
        total += animal.appetite
    return total
