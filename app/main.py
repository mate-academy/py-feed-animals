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
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(animals):
    sum_of_animal_appetite = 0
    for animal in animals:
        if animal.is_hungry is True:
            sum_of_animal_appetite += animal.appetite
            animal.is_hungry = False
    return sum_of_animal_appetite
