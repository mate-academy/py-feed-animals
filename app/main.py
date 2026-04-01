class Animal:
    animals = []

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.is_hungry:
            return 0
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = not self.is_hungry
        return self.appetite


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3)
        if not is_hungry:
            self.feed()

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7)
        if not is_hungry:
            self.feed()

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list | Animal) -> int:
    eat_points = 0
    for animal in animals:
        if not animal.is_hungry:
            continue
        animal.feed()
        eat_points += animal.appetite
    return eat_points
