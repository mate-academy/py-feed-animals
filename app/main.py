from __future__ import annotations


class Animal:
    def __init__(self, name: str,
                 appetite: int = 0,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.is_hungry = is_hungry
        self.appetite = appetite

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        self.appetite = 0
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str,
                 is_hungry: bool = True,
                 appetite: int = 3) -> None:
        appetite = 3
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 is_hungry: bool = True,
                 appetite: int = 7) -> None:
        appetite = 7
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(lst_animals: list[Animal]) -> int:
    result = 0
    for animal in lst_animals:
        result += animal.feed()

    return result
