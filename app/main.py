class Animal:
    def __init__(self, name, appetite, is_hungry):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I`m {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite = 3, is_hungry=is_hungry)

    def catch_mouse(self):
        print(f"The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite = 7, is_hungry=is_hungry)

    def bring_slippers (self):
        print(f"The slippers delivered!")

def feed_animal(animals):
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food