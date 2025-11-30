class Animal:
    """
    Base class for all animals.
    Represents a generic animal that can be fed and identified by name.

    Attributes:
        name (str): The name of the animal.
        appetite (int): Amount of food points required for the animal
        to become full.
        is_hungry (bool): Indicates whether the animal is hungry.
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
        Prints the animal's name in the format:
        "Hello, I'm {name}"

        :return: None
        """

        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Feeds the animal if it is hungry.
        When the animal is hungry, the method:
         - prints how many food points it is eating
         - sets `is_hungry` to False
         - returns the number of consumed food points

        When the animal is not hungry, the method:
         - prints nothing
         - returns 0

        :return: The number of food points consumed.
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

        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    # noinspection PyMethodMayBeStatic
    def catch_mouse(self) -> None:
        """
        Prints a message indicating that the cat starts hunting a mouse.

        :return: None
        """

        print("The hunt began!")


class Dog(Animal):

    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:

        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    # noinspection PyMethodMayBeStatic
    def bring_slippers(self) -> None:
        """
        Prints a message indicating that the dog brings slippers.

        :return: None
        """

        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    """
    Feeds all animals in the provided list.
    For each animal:
     - the animal's `feed()` method is called
     - the returned food points are added to the total

    Only hungry animals contribute to the total amount of food points,
    since non-hungry animals return 0.

    :param animals: A list of animals that implement the `feed()` method.

    :return: The total number of food points consumed by all animals.
    """

    return sum(animal.feed() for animal in animals)
