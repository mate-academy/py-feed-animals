class Animal:

    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):

    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=7)
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(ls_of_animals: list):
    sum_of_hungry = 0
    for animal in ls_of_animals:
        if animal.is_hungry:
            sum_of_hungry += animal.appetite
            animal.is_hungry = False
    return sum_of_hungry
