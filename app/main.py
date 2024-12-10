class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        """
        Initialize an Animal instance.

        :param name: The name of the animal.
        :param appetite: The food points needed to be full.
        :param is_hungry: Indicates if the animal is hungry (default: True).
        """
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Print the name of the animal."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Feed the animal if it's hungry.

        :return: The number of food points eaten, or 0 if not hungry.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """
        Initialize a Cat instance.

        :param name: The name of the cat.
        :param is_hungry: Indicates if the cat is hungry (default: True).
        """
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        """Simulate catching a mouse."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """
        Initialize a Dog instance.

        :param name: The name of the dog.
        :param is_hungry: Indicates if the dog is hungry (default: True).
        """
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        """Simulate bringing slippers."""
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    """
    Feed a list of animals.

    :param animals: List of Animal instances.
    :return: The total food points needed to feed all hungry animals.
    """
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food
