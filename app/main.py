from __future__ import annotations


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

        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite

        if self.is_hungry is False:
            self.appetite = 0
            return self.appetite


class Cat(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 3,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 7,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite)
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list[Animal]) -> int:
    result = 0
    for point_of_food in list_of_animals:
        point_of_food.feed()
        result += point_of_food.appetite

    return result
