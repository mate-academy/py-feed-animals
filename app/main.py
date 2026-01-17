class Animal:
    animals = []
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")
    # feed() should print Eating {appetite} food points...,
    # set is_hungry to False and return number of eaten food points if animal is hungry.
    # Otherwise, it should return 0 and print nothing
    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


def feed_animals(list_of_animals: list) -> int:
    appetite = 0
    for animal in Animal.animals:
        if animal in list_of_animals:
            if animal.is_hungry:
                appetite += animal.appetite
                animal.feed()

    return appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")
