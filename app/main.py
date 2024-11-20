from typing import Union


class Animal:

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> Union[int, None]:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
        else:
            self.appetite = 0

        return self.appetite


class Cat(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    return sum([Animal.feed(animal) for animal in animals])
