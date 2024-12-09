
class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry = True) -> None:
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
        return 0


class Cat(Animal):
    def __init__(self, name : str,
                 is_hungry : bool = True) -> None:
        super().__init__(name, appetite = 3, is_hungry = is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name : str,
                 is_hungry : bool = True) -> None:
        super().__init__(name, appetite = 7, is_hungry = True)

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")

def feed_animals(animals) -> None:
    total_food = 0
    for animal in animals:
        eaten_food = animal.feed()
        total_food += eaten_food
    return total_food
