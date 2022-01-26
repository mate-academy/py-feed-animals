class Animal:

    def __init__(self, name, appetite: int, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        print(f"Eating {self.appetite} food points...")
        if self.appetite:
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):

    def __init__(self, name, is_hungry=True):
        self.name = name
        self.is_hungry = is_hungry
        super(Cat, self).__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name, is_hungry=True):
        self.name = name
        self.is_hungry = is_hungry
        super(Dog, self).__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(animals):
    need_to_feed = 0
    for animal in animals:
        if animal.is_hungry is True:
            need_to_feed += animal.appetite
    return need_to_feed
