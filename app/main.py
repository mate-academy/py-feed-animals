from typing import List


class Animal:
    def __init__(self, name: str, appetite: int = 0, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            meal_points = self.appetite
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.appetite = 0
            return meal_points
        return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    total_appetite = 0
    for animal in animals:
        total_appetite += animal.feed()
    return total_appetite
