class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> str | int:
        if self.is_hungry:
            self.is_hungry = not self.is_hungry
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True,
                 appetite: int = 3) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True,
                 appetite: int = 7) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    return sum(Animal.feed(animal) for animal in animals)
