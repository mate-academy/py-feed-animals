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
        else:
            return 0


class Cat(Animal):
    def __init__(self, name, appetite=3, is_hungry=True):
        super(Cat, self).__init__(name, appetite, is_hungry=True)

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, appetite=7, is_hungry=True):
        super(Dog, self).__init__(name, appetite, is_hungry=True)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list):
    points = []
    for animal in animals:
        points.append(Animal.feed(animal))
    return sum(points)
