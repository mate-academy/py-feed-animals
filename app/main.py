#  write your code here
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
            decrease_food = self.appetite
            print(f"Eating {decrease_food} food points...")
            self.is_hungry = False
            return decrease_food
        return 0


class Cat(Animal):

    def __init__(
            self,
            name: str,
            appetite: int = 3,
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

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    food_amount = 0
    for animal in animals:
        food_amount += animal.feed()
    return food_amount
