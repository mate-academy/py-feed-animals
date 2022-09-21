class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name, is_hungry=True, appetite=3):
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        if self.is_hungry:
            self.is_hungry = False
            print("The hunt began!")
        else:
            return 0


class Dog(Animal):
    def __init__(self, name, is_hungry=True, appetite=7):
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        if self.is_hungry:
            self.is_hungry = False
            print("The slippers delivered!")
        else:
            return 0


def feed_animals(animals):
    result = []
    for animal in animals:
        if animal.is_hungry:
            result.append(animal.appetite)
            animal.is_hungry = False
    return sum(result)
