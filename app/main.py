from typing import List


class Animal:
    def __init__(
        self,
        name: str,
        appetite: int,
        is_hungry: bool = True,
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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name}, appetite={self.appetite}, "
            f"hungry={self.is_hungry})"
        )


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
