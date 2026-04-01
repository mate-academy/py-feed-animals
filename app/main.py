class Animal:
    def __init__(self, name, appetite=0, is_hungry=True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name="Cat", appetite=3, is_hungry=True) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        if self.is_hungry:
            self.appetite = 0
            print("The hunt began!")


class Dog(Animal):
    def __init__(self, name="Dog", appetite=7, is_hungry=True) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        if self.is_hungry:
            print("The slippers delivered!")


def feed_animals(animals: list[Animal]):
    total = 0
    for animal in animals:
        total += animal.feed()
    return total
