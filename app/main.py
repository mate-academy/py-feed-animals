class Animal:
    def __init__(self, name, appetite, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name, is_hungry: bool = True):
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry: bool = True):
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list):
    food_to_feed_all = 0
    for animal in animals:
        food_to_feed_all += animal.feed()
    return food_to_feed_all
