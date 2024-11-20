class Animal:
    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.is_hungry = is_hungry
        self.appetite = appetite

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
            is_hungry: bool = True,
            appetite: int = 3
    ) -> None:
        super().__init__(name, is_hungry=is_hungry, appetite=appetite)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
            appetite: int = 7
    ) -> None:
        super().__init__(name, is_hungry=is_hungry, appetite=appetite)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals_to_feed: list) -> int:
    points = 0
    for animal in animals_to_feed:
        if animal.is_hungry:
            points += animal.appetite
            animal.feed()
    return points
