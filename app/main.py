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
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.appetite <= 0 or not self.is_hungry:
            return 0
        print(f"Eating {self.appetite} food points...")
        eat_food = self.appetite
        self.appetite -= self.appetite
        self.is_hungry = not self.is_hungry
        return eat_food


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super(Cat, self).__init__(name=name, appetite=3)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super(Dog, self).__init__(name=name, appetite=7)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    all_food = 0
    for animal in animals:
        all_food += animal.feed()

    return all_food
