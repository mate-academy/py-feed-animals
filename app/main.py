class Animal:

    def __init__(
            self, name: str, appetite: int,
            is_hungry: bool = True) -> None:

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

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
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    need_for_food = 0

    for animal in animals:
        if animal.is_hungry:
            need_for_food += animal.feed()

    return need_for_food
