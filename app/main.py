from __future__ import annotations


class Animal:
    def __init__(self, *args, **kwargs) -> None:
        self.is_hungry = True
        self.appetite = 0
        if len(args) > 0:
            self.name = args[0]
        if len(args) > 1:
            self.appetite = args[1]
        if len(args) > 2: 
            self.is_hungry = args[2]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "appetite" in kwargs:
            self.appetite = kwargs["appetite"]
        if "is_hungry" in kwargs:
            self.is_hungry = kwargs["is_hungry"]

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
    return sum([animal.feed() for animal in animals])