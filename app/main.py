from __future__ import annotations
from typing import Generator

class Animal:
    def __init__(self, name: str, appetite: int, is_hungry = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry and appetite > 0
        
    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        appetite = 0
        if self.is_hungry:
            appetite = self.appetite
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
        return appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(feeding_generator(animals))

    
def feeding_generator(animals: list[Animal]) -> Generator[int, None, None]:
    for animal in animals:
        yield animal.feed()