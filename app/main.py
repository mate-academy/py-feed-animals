class Animal:

    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is False:
            return 0
        if self.is_hungry is True:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite


class Cat(Animal):
    def __init__(self, name, appetite=3, is_hungry=True):
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, appetite=7, is_hungry=True):
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(list_of_animals):
    sum_of_food_points = 0
    for animal in list_of_animals:
        if animal.is_hungry:
            sum_of_food_points += animal.appetite
            Animal.feed(animal)

    return sum_of_food_points
