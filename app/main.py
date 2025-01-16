#  write your code here
class Animal:
    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.is_hungry = is_hungry
        self.appetite = appetite
        self.name = name

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        food_used = 0
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            food_used = self.appetite
            self.is_hungry = False
        return food_used


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    sum_feed = 0
    for animal in animals:
        sum_feed += animal.feed()

    return sum_feed
