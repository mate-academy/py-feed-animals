class Animal:
    """
    Represents a basic Animal creature.

    Attributes:
    ----------
    name : str
        the name of the animal
    appetite : int
        the food points the animal needs to eat to be fine
    is_hungry : bool
        indicates if the animal is ready to eat

    Methods:
    -------
    print_name()
        prints the animal's name
    feed()
        if the Animal's "is_hungry" is True, prints the message about
        feeding and returns the number of points the Animal has eaten.
        Otherwise, returns 0.
    """

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
        """
        Prints a hello message with animal's name.
        :return: None
        """
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        If the animal's "is_hungry" is True, prints the message about
        feeding and returns the number of points the Animal has eaten.
        Otherwise, returns 0.
        Sets "is_hungry" to False.
        :return:
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
        super().__init__(name=name, appetite=3)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        """
        Prints a message about Cat's hunting.
        :return: None
        """
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, is_hungry)
        if is_hungry:
            self.appetite = 7
        else:
            self.appetite = 0

    @staticmethod
    def bring_slippers() -> None:
        """
        Prints a message about bringing slippers.
        :return: None
        """
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals if animal.is_hungry)
