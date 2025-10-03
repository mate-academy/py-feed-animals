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

    def feed(self):
        if self.appetite > 0:
            print(f"Eating {self.appetite} food points...")
            eaten_points = self.appetite
            self.appetite = 0
            self.is_hungry = False
            return eaten_points

        return self.appetite

class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")

def feed_animals(list_of_animals: list[Animal]) -> int:
    total_fed_points: int = 0
    for animal in list_of_animals:
        if animal.appetite and animal.is_hungry is True:
            appetite_points = animal.feed()
            total_fed_points += appetite_points
    return total_fed_points
