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
        if not self.is_hungry:
            return 0

        self.is_hungry = False
        food_points = self.appetite
        self.appetite -= food_points
        print(f"Eating {food_points} food points...")
        return food_points


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(
            name=name,
            is_hungry=is_hungry,
            appetite=3
        )

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(
            name=name,
            is_hungry=is_hungry,
            appetite=7
        )

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum([animal.feed() for animal in animals])
