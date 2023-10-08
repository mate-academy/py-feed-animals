class Animal:
    animals = []

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:

        self.name = name
        self.is_hungry = is_hungry
        self.appetite = appetite
        self.animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        food_points = 0

        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            food_points += self.appetite

            return food_points

        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7)
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: Animal.animals) -> int:
    total_food_points = 0

    for animal in animals:
        total_food_points += animal.feed()

    return total_food_points
