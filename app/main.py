class Animal:

    list_of_animals = []

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.list_of_animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        return 0


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
            name: str,
            is_hungry: bool = True,
            appetite: int = 7
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list[Animal]) -> int:
    return sum([animal.feed() for animal in list_of_animals])
