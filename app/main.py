from functools import reduce


class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if not self.appetite or not self.is_hungry:
            return 0

        food_points_to_eat = self.appetite

        print(f"Eating {food_points_to_eat} food points...")

        self.is_hungry = False
        self.appetite -= food_points_to_eat

        return food_points_to_eat


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 3, is_hungry)

    @classmethod
    def catch_mouse(cls) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 7, is_hungry)

    @classmethod
    def bring_slippers(cls) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]):
    return reduce(lambda previous_value, current_value: previous_value + current_value.feed(), animals, 0)
