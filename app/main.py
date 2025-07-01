class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        self.food_points = 0

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.name and self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.food_points = self.appetite
            return self.food_points
        if self.name and not self.is_hungry:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_animal: ["Animal"]) -> int:
    total_appetite = 0
    for animal in list_animal:
        if animal.is_hungry:
            animal.feed()
            total_appetite += animal.appetite
    return total_appetite
