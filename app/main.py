class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        return print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is True and self.appetite > 0:
            print(f"Eating {self.appetite} food points...")
            appetite = self.appetite
            self.appetite = 0
            self.is_hungry = False
            return appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True, appetite: int = 3):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse():
        return print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True, appetite: int = 7):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers():
        return print("The slippers delivered!")


def feed_animals(animals_list: list):
    food_points = 0
    for animal in animals_list:
        if animal.is_hungry:
            food_points += animal.appetite
            animal.feed()
    return food_points
