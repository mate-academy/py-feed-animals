class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if not self.is_hungry:
            return 0
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = False
        points_eaten, self.appetite = self.appetite, 0
        return points_eaten


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name=name, appetite=0 if not is_hungry else 3)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name=name, appetite=0 if not is_hungry else 7)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(animals: list):
    sum_of_points = 0
    for animal in animals:
        sum_of_points += animal.feed()
    return sum_of_points
