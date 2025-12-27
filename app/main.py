class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Print the animal's name."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Feed the animal if it is hungry.
        Returns the number of food points eaten.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        """Simulate catching a mouse."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        """Simulate bringing slippers."""
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    """
    Feed all hungry animals in the list.
    Returns the total number of food points eaten.
    """
    total_food_points = 0
    for animal in animals:
        total_food_points += animal.feed()
    return total_food_points


