from typing import List


class Animal:
    def __init__(
            self, name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")
        return None

    def feed(self) -> None:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")
        return None


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")
        return None


def feed_animals(list_of_animals: List[Animal]) -> int:
    food_needed = 0
    for animal in list_of_animals:
        if animal.is_hungry is True:
            food_needed += animal.appetite
        animal.feed()
    return food_needed
