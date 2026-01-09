class Animal:
    def __init__(self, name : str = "default",
                 appetite : int = 1,
                 is_hungry : bool = True) -> None:
        self.name : str = name
        self.appetite : int = appetite
        self.is_hungry : bool = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str = "default", is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str = "default", is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals : list["Animal"]) -> int:
    result = 0
    for animal in animals:
        result += animal.feed()
    return result
