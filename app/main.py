from __future__ import annotations


class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> Animal:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> str:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True,
                 appetite: int = 3) -> Cat:
        super().__init__(name, appetite, is_hungry)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True,
                 appetite: int = 7) -> Dog:
        super().__init__(name, appetite, is_hungry)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list) -> int:
    result_list = []
    for animal in list_of_animals:
        if animal.is_hungry:
            animal.feed()
            result_list.append(animal.appetite)
    return sum(result_list)
