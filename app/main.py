class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.appetite or not self.is_hungry:
            return 0

        food_points_to_eat = self.appetite

        print(f"Eating {food_points_to_eat} food points...")

        self.is_hungry = False
        self.appetite -= food_points_to_eat

        return food_points_to_eat


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @classmethod
    def catch_mouse(cls) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @classmethod
    def bring_slippers(cls) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    food_points = 0

    for animal in animals:
        food_points += animal.feed()

    return food_points
