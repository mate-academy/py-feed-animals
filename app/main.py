class Animal:
    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, is_hungry)
        self.is_hungry = is_hungry
        self.appetite = 3

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, is_hungry)
        self.is_hungry = is_hungry
        self.appetite = 7

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    necessary_points = 0

    for animal in animals:
        if animal.is_hungry:
            necessary_points += animal.feed()

    return necessary_points
