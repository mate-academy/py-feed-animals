class Animal:
    def __init__(
            self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        eaten = 0
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            eaten = self.appetite
            self.is_hungry = False
            self.appetite = 0
        return eaten


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry=is_hungry, appetite=3)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry=is_hungry, appetite=7)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    food = 0
    for animal in animals:
        food += animal.feed()
    return food
