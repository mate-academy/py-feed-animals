class Animal:
    def __init__(self, name: str,
                 appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        if is_hungry:
            self.appetite = appetite
        else:
            self.appetite = 0
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            appetite = self.appetite
            self.appetite = 0
            return appetite
        else:
            return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        if is_hungry:
            super().__init__(name, 3, is_hungry)
        else:
            super().__init__(name, 0, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        if is_hungry:
            super().__init__(name, 7, is_hungry)
        else:
            super().__init__(name, 0, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    sum_feed_points = 0
    for animal in animals:
        sum_feed_points += animal.appetite
        animal.feed()
    return sum_feed_points
