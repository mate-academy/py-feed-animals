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
        else:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite


class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=3)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=7)
        self.name = name
        self.is_hungry = is_hungry

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(all_animal):
    amount = 0
    for animal in all_animal:
        amount += animal.feed()
    return amount
