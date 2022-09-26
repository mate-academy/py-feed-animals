class Animal:
    def __init__(self, name, appetite: int, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    food_points = sum([Animal.feed(feed) for feed in animals])
    return food_points
