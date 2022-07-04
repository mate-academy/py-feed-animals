class Animal:
    def __init__(self, name: str, appetite: int, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        return f"Hello, I'm {self.name}"

    def feed(self):
        self.is_hungry = False
        return f"Eating {self.appetite} food points..."

class Cat(Animal):

        def __init__(self, ):

        def catch_mouse(self):
            return f"The hunt began!"


class Dog(Animal):

    def __init__(self, ):

    def bring_slippers:
        return f"The slippers delivered!"