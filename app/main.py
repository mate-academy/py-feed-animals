class Animal:
    def __init__(self, name: str,
                 appetite: int = 0, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        eaten = 0
        if self.is_hungry:
            eaten = self.appetite
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
        return eaten


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name)
        self.appetite = 3
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name)
        self.is_hungry = is_hungry
        self.appetite = 7

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    food_total = 0
    for animal in animals:
        food_total += animal.feed()
    return food_total
