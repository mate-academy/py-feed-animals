class Animal:
    def __init__(
        self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self. appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.is_hungry:
            return 0

        print(f"Eating {self.appetite} food points...")
        eaten_food_points = self.appetite
        self.is_hungry = False
        self.appetite = 0
        return eaten_food_points


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(
            name=name,
            appetite=3,
            is_hungry=is_hungry
        )

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(
            name=name,
            appetite=7,
            is_hungry=is_hungry
        )

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
