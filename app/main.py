from typing import List


class Animal:
    """
    Class  that represents animal that can eat.
    """
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        """Function that prints information about animal name."""
        print(f"Hello, I'm {self.name}")

    def feed(self):
        """Function for eating given number of point."""
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite

        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse():
        """Function to inform about catching mouse."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers():
        """Function to inform about bringing slippers."""
        print("The slippers delivered!")


def feed_animals(animals_list: List[Animal]) -> int:
    """
    Function to feed all animals in list and return sum of food needed.
    :param animals_list: animals to be fed
    :return: sum of food needed
    """
    return sum([animal.feed() for animal in animals_list])