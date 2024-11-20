class Animal:

    def __init__(
        self,
        name: str,
        appetite: int,
        is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
        self.is_hungry = not self.is_hungry
        return 0 if self.is_hungry else self.appetite


class Cat(Animal):

    def __init__(
        self,
        name: str,
        is_hungry: bool = True,
        appetite: int = 3
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
        self,
        name: int,
        is_hungry: bool = True,
        appetite: int = 7
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    resalt = 0
    for animal in animals:
        resalt += animal.feed()
    return resalt
