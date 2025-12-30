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

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> str:
        if not self.is_hungry:
            return 0
        self.is_hungry = False
        print(f"Eating {self.appetite} food points...")
        return self.appetite


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name=name, is_hungry=is_hungry, appetite=3)

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name=name, is_hungry=is_hungry, appetite=7)

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> str:
    return sum(animal.feed() for animal in animals)
