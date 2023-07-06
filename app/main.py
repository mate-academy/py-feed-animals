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
        if self.appetite != 0 and self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            appetite_points = self.appetite

            self.is_hungry = not self.is_hungry
            self.appetite = 0
            return appetite_points

        return 0


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
    ) -> None:
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
    ) -> None:
        super().__init__(name, appetite=7)
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals_list: list[Animal]) -> int:
    total_food_points = sum(animal.feed() for animal in animals_list)
    return total_food_points
