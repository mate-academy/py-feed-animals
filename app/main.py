class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            return_result = self.appetite
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.appetite = 0
            return return_result
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    list_food_points = []
    for animal in animals:
        food_points = animal.feed()
        list_food_points.append(food_points)
    return sum(list_food_points)
