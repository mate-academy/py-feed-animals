class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = not self.is_hungry
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, appetite=7)
        self.name = name
        self.is_hungry = is_hungry

    def bring_slippers(self):
        print("The slippers delivered!")
