class Animal:

    def __init__(
            self,
            name: str,
            appetite: int = 0,
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
        else:
            return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry=is_hungry, appetite=7)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(list_animals: list[Animal]) -> int:
    sum_food = 0
    for animal in list_animals:
        if animal.is_hungry:
            sum_food += animal.appetite
            animal.feed()
    return sum_food
