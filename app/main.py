class Animal:
    def __init__(
        self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> None:
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
        animal.feed()
    return total_food


elephant = Animal("Elephant", 100)
rat = Animal("Rat", 1)
lion = Animal("Lion", 25)
cat = Cat("Cat", False)

food_points = feed_animals([elephant, rat, lion, cat])
print("food points:", food_points)
