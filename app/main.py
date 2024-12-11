from typing import List


class Animal:
    animals_list = []

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animals_list.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        else:
            return 0


class Cat(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)
        self.appetite = appetite

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)
        self.appetite = appetite

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: List[Animal]) -> int:
    sum_food_points = 0

    for animal in list_of_animals:
        if animal.is_hungry:
            sum_food_points += animal.appetite
            animal.feed()

    return sum_food_points
