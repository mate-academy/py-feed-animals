"""Feed animals: Animal base class with Cat and Dog children."""


class Animal:
    """A base animal that can be hungry and fed."""

    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Print a short greeting with the animal's name."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """Feed the animal if it is hungry.

        Returns the number of food points eaten, or 0 if the
        animal was already full (and prints nothing in that case).
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        """Start the hunt."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        """Bring the slippers."""
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    """Feed every animal in the list, return total food points used."""
    return sum(animal.feed() for animal in animals)
