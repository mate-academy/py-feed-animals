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
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            points = self.appetite
            self.appetite = 0
            return points
        return 0


class Cat(Animal):
    def __init__(self, name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals_list: list) -> int:
    return sum(animal.feed() for animal in animals_list)
