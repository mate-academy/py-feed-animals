"""Module for feeding animals."""
from __future__ import annotations


class Animal:
    """A representation of an animal."""

    @staticmethod
    def feed_animals(animals: list[Animal]) -> int:
        """Feed a list of animals.

        :param animals: A list of animals to feed.
        :type animals: list[Animal]
        :return: The total amount of food eaten.
        :rtype: int
        """
        return sum(
            animal.feed()
            for animal in animals
        )

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        """Initialize an animal.

        :param name: The name of the animal.
        :type name: str
        :param appetite: The amount of food the animal eats.
        :type appetite: int
        :param is_hungry: Whether the animal is hungry.
        :type is_hungry: bool
        """
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Print the name of the animal."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """Feed the animal.

        :return: The amount of food eaten.
        :rtype: int
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False

            return self.appetite

        return 0


class Cat(Animal):

    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        """Initialize a cat.

        :param name: The name of the cat.
        :type name: str
        :param is_hungry: Whether the cat is hungry.
        :type is_hungry: bool
        """
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        """Catch a mouse."""
        print("The hunt began!")


class Dog(Animal):

    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        """Initialize a dog.

        :param name: The name of the dog.
        :type name: str
        :param is_hungry: Whether the dog is hungry.
        :type is_hungry: bool
        """
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        """Bring slippers."""
        print("The slippers delivered!")


feed_animals = Animal.feed_animals
