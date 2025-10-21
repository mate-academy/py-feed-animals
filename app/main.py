class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.is_hungry:
            return 0

        print(f"Eating {self.appetite} food points...")
        self.is_hungry = False
        return self.appetite

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(name={self.name}, "
                f"appetite={self.appetite}, "
                f"is_hungry={self.is_hungry})")


class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True,
                 appetite: int = 3) -> None:
        appetite = appetite if is_hungry else 0
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True,
                 appetite: int = 7) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
