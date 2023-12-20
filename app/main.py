class Animal:
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
        print("Hello, I'm", self.name)

    def feed(self) -> int:
        if self.is_hungry:
            print("Eating", self.appetite, "food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 3,
            is_hungry: bool = True
    ) -> None:
        self.appetite = appetite
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 7,
            is_hungry: bool = True
    ) -> None:
        self.appetite = appetite
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    total_food = 0
    for animal in animals:
        if isinstance(animal, Animal) and animal.is_hungry:
            animal_food = animal.feed()
            total_food += animal_food
    return total_food


if __name__ == "__main__":
    cat = Cat("Tom")
    dog = Dog("Rex")
    pantera = Animal("Bagira", 25)

    animals = (cat, dog, pantera)

    feed_animals(animals)
