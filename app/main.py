class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            food_points = self.appetite
            self.appetite = 0
            self.is_hungry = False
            return food_points
        return 0


class Cat(Animal):
    def __init__(self, name, appetite: int = 3, is_hungry: bool = True):
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, appetite: int = 7, is_hungry: bool = True):
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list):
    food_points = 0
    for animal in animals:
        food_points += animal.feed()
    return food_points
