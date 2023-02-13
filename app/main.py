class Animal:

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        super().__init__()
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        super().__init__()
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        else:
            return 0


class Cat(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Cat, Dog]) -> int:
    total_appetite = 0
    for animal in animals:
        total_appetite += animal.feed()
    return total_appetite
