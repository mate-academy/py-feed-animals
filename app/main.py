class Animal:
    def __init__(
            self, name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 3,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            appetite: int = 7,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(some_animals: list[Animal]) -> int:
    return sum([animal.feed() for animal in some_animals])
