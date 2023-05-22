class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self._name = name
        self._appetite = appetite
        self._is_hungry = is_hungry

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_hungry(self) -> bool:
        return self._is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self._name}")

    def feed(self) -> int:
        if not self._is_hungry:
            return 0
        print(f"Eating {self._appetite} food points...")
        self._is_hungry = False
        return self._appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
