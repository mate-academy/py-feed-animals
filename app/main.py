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

    def feed(self) -> None:
        food_points = 0
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            food_points += self.appetite
        return food_points


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


def feed_animals(animal_list: list[Animal]) -> int:
    total_points = 0
    for animal in animal_list:
        total_points += animal.feed()
    return total_points
