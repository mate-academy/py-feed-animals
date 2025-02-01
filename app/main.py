from __future__ import annotations


class Animal:
    def __init__(self, *args, **kwargs) -> None:
        self.is_hungry = True
        self.apetite = 0
        if len(args) > 0:
            self.name = args[0]
        if len(args) > 1:
            self.apetite = args[1]
        if len(args) > 2: 
            self.is_hungry = args[2]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "apetite" in kwargs:
            self.apetite = kwargs["apetite"]
        if "is_hungry" in kwargs:
            self.is_hungry = kwargs["is_hungry"]

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        apetite = 0
        if self.is_hungry:
            apetite = self.apetite
            self.is_hungry = False
            print(f"Eating {self.apetite} food points...")
        return apetite


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