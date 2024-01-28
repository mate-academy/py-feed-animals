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
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        super().__init__(name, 3)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        super().__init__(name, 7)
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    sum_of_food_points = 0
    for animal in animals:
        for key, value in animal.__dict__.items():
            if key == "appetite" and animal.is_hungry:
                sum_of_food_points += value
        animal.feed()
    return sum_of_food_points
