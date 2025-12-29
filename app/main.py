class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        print(f"Eating {self.appetite} food points...")
        if self.is_hungry:
            self.is_hungry = False
            return self.appetite
        return 0

class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print(f"The hunt began!")

class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print(f"The slippers delivered!")

    @staticmethod
    def feed_animals(animals: list) -> int:
        total_points_food = 0
        for animal in animals:
            total_points_food += animal.feed()
        return total_points_food
