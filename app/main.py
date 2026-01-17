class Animal:
    def __init__(
            self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Prints the animal's name."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Feeds the animal if it is hungry.
        :return: The number of food points eaten if hungry, otherwise 0.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        """Prints a message indicating the cat has started hunting."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        """Prints a message indicating the dog has brought slippers."""
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    """
    Feeds a list of animals and returns the total amount of food consumed.
    """
    return sum(animal.feed() for animal in animals)
