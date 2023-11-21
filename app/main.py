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
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
        else:
            return 0
        self.is_hungry = not self.is_hungry
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7)
        self.name = name
        self.is_hungry = is_hungry

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    total_food_points = 0

    for animal in animals:
        food_points = animal.feed()
        total_food_points += food_points

    return total_food_points
