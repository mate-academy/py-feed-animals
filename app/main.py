from typing import List


class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(name=self.name, appetite=3, is_hungry=self.is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(name=self.name, appetite=7, is_hungry=self.is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    sum_points = 0
    for animal in animals:
        sum_points += animal.feed()
    return sum_points
