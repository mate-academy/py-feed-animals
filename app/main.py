class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        is_hungry = True

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
        else:
            self.appetite = 0
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, appetite=3, is_hungry=True)
        self.is_hungry = is_hungry
        is_hungry = True

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, appetite=7, is_hungry=True)
        self.is_hungry = is_hungry
        self.is_hungry = True

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    return sum(animal for animal in animals)
