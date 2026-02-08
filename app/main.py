class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            points = self.appetite
            self.is_hungry = False
            return points
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = 3
        self.is_hungry = is_hungry
    def catch_mouse(self):
        print(f"The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = 7
        self.is_hungry = is_hungry

    def bring_slippers(self):
        print(f"The slippers delivered!")


def feed_animals(animal_list):
    total_food = 0
    for animal in animal_list:
        if animal.is_hungry:
            points = animal.eat()
            total_food += points
    return total_food
