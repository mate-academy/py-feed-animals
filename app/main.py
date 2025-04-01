class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) \
            -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Prints the animal's name in a formatted string."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """Feeds the animal if it's hungry, returns food points consumed."""
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0  # If not hungry, return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        """Prints a message indicating the cat is hunting."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        """Prints a message indicating the dog delivered the slippers."""
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    total_food = sum(animal.feed() for animal in animals)
    return total_food
