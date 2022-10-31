from __future__ import annotations
from typing import Union


class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> Union[Animal, int]:
        if not self.is_hungry:
            return 0
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = False
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str, appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list) -> int:
    total_appetite = 0
    for animal in list_of_animals:
        if animal.is_hungry:
            total_appetite += animal.appetite
        Animal.feed(animal)
    return total_appetite
