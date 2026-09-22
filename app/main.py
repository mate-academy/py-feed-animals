class Animal:
    def __init__(
        self,
        name: str,
        appetite: int = 0,
        is_hungry: bool = True,
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")
        return f"Hello, I'm {self.name}"

    def feed(self) -> int:
        if not self.is_hungry:
            return 0

        print(f"Eating {self.appetite} food points...")
        self.is_hungry = False

        return self.appetite


class Cat(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True,
        appetite: int = 3,
    ) -> None:
        super().__init__(name=name, appetite=appetite, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True,
        appetite: int = 7,
    ) -> None:
        super().__init__(name=name, appetite=appetite, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    count = 0
    for animal in animals:
        count += animal.feed()
    return count
