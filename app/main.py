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
            return self.appetite

        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, is_hungry=is_hungry, appetite=3)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, is_hungry=is_hungry, appetite=7)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Cat | Dog]) -> int:
    return sum(animal.feed() for animal in animals)
