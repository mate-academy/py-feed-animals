class Animal:
    def __init__(
        self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        appetite = self.appetite
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.appetite = 0
            return appetite
        else:
            return 0


class Cat(Animal):
    def __init__(
        self, name: str, is_hungry: bool = True, appetite: int = 3
    ) -> None:
        super(Cat, self).__init__(
            name=name, is_hungry=is_hungry, appetite=appetite
        )

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
        self, name: str, is_hungry: bool = True, appetite: int = 7
    ) -> None:
        super(Dog, self).__init__(
            name=name, is_hungry=is_hungry, appetite=appetite
        )

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    sum_food = 0
    for animal in animals:
        sum_food += animal.feed()
    return sum_food
