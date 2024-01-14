class Animal:
    def __init__(
        self,
        name: str,
        appetite: int,
        is_hungry: bool = True,
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        appetite = self.appetite if self.is_hungry else 0
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.appetite = 0

        return appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    sum_of_appetite = 0

    for animal in animals:
        if animal.is_hungry:
            sum_of_appetite += animal.feed()

    return sum_of_appetite
