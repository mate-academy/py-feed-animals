class Animal:
    list_of_animals = []

    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.list_of_animals.append(self)

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            self.is_hungry = False
            return 0


class Cat(Animal):
    def __init__(self, name, appetite=3, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

        Cat.feed(self)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, appetite=7, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(list_of_animals):
    sum_feed_points = 0
    for i in list_of_animals:
        if i.is_hungry is True:
            sum_feed_points += i.appetite
            i.is_hungry = False
    return sum_feed_points
