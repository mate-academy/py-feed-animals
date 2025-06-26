from typing import List


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
        if self.appetite > 0 and self.is_hungry is True:
            count_of_food = self.appetite
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.appetite = 0
            return count_of_food
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    amount_of_food = 0
    for animal in animals:
        amount_of_food += animal.feed()
    return amount_of_food
