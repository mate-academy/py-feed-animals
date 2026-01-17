class Animal:
    def __init__(
            self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.is_hungry:
            return 0
        print(f"Eating {self.appetite} food points...")
        appetite_points = self.appetite
        self.appetite = 0
        self.is_hungry = False
        return appetite_points


class Cat(Animal):
    def __init__(
            self, name: str, appetite: int = 3, is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self, name: str, appetite: int = 7, is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list) -> int:
    return sum(animal.feed() for animal in list_of_animals)
