class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            self.food_points = int(self.appetite)
            self.appetite = 0
            return self.food_points
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str,
                 appetite: int = 3,
                 is_hungry: bool = True):
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 appetite: int = 7,
                 is_hungry: bool = True):
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    needed_feed = 0
    for animal in animals:
        if animal.is_hungry:
            needed_feed += animal.appetite
            animal.feed()
    return needed_feed
