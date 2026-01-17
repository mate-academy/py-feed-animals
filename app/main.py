class Animal:

    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.appetite > 0 and self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            result = self.appetite
            self.appetite = 0
            return result
        return 0


class Cat(Animal):

    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=3)
        self.name = name
        self.appetite = 3
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name, is_hungry=True):
        super().__init__(name, appetite=7)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")


def feed_animals(anim_list: list):
    result = 0
    for animal in anim_list:
        result += Animal.feed(animal)
    return result
