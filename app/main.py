class Animal:
    def __init__(
            self, name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None | int:
        food_point = 0
        if self.is_hungry:
            self.is_hungry = False
            food_point = self.appetite
            print(f"Eating {self.appetite} food points...")
            self.appetite = 0
        return food_point


class Cat(Animal):
    def __init__(
            self,
            name: str, appetite: int = 3,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 7,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list) -> int:
    sum_point_food = 0

    for animal in list_of_animals:
        sum_point_food += animal.feed()

    return sum_point_food
