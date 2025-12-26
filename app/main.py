class Animal:
    def __init__(
            self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:
        """
        Initializes the animal with a name, appetite, and hunger status.
        """
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """
        Prints the name of the animal in the format: "Hello, I'm {name}".
        """
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Feeds the animal if it's hungry and returns the food points consumed.
        If the animal is not hungry, it returns 0.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """
        Initializes the cat with a fixed appetite of 3 food points.
        """
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        """
        Prints that the cat has begun hunting.
        """
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """
        Initializes the dog with a fixed appetite of 7 food points.
        """
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        """
        Prints that the dog has brought slippers.
        """
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    """
    Feeds all the hungry animals from the list and returns the total number of
    food points consumed.
    """
    total_food_points = 0
    for animal in animals:
        total_food_points += animal.feed()
    return total_food_points


# Example usage:
if __name__ == "__main__":
    cat = Cat("Cat")
    lion = Animal("Lion", 25)
    dog = Dog("Dog")

    cat.print_name()  # "Hello, I'm Cat"
    print(cat.feed())  # "Eating 3 food points"
    print(cat.is_hungry)  # False

    lion.print_name()  # "Hello, I'm Lion"
    print(lion.feed())  # "Eating 25 food points"
    print(lion.is_hungry)  # False

    dog.print_name()  # "Hello, I'm Dog"
    print(dog.feed())  # "Eating 7 food points"
    print(dog.is_hungry)  # False

    # Feeding all animals together
    total_food_points = feed_animals([cat, lion, dog])
    print(f"Total food points consumed: {total_food_points}")  # 35
