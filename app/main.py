class Animal:
    def __init__(
            self, name: str,
            appetite: int,
            is_hungry: bool = True
            ):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        return f"Hello, I'm {self.name} "
    
    def feed(self) -> str | int:
        if self.is_hungry == True:
            self.is_hungry = not self.is_hungry
            return f"Eating {self.appetite} food points..."
        return 0


class Cat(Animal):
    def __init__(self, name, is_hungry = True):
        super().__init__(
            name,
            appetite=3,
            is_hungry=is_hungry
            )

    def catch_mouse(self) -> None:
        print("The hunt began!")
    
class Dog(Animal):
    def __init__(self, name, is_hungry = True):
        super().__init__(
            name,
            appetite=7,
            is_hungry=is_hungry
            )

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    digit = 0
    for animal in animals:
        if animal.is_hungry is True:
          digit += animal.appetite
    return digit
