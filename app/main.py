class Animal:
    def __init__(
            self, name: str, appetite: int, is_hungry: bool = True
    ) -> None:

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print("Hello, I'm {name}".format(name=self.name))

    def feed(self) -> int:
        if self.is_hungry:
            print(
                "Eating {appetite} food points..."
                .format(appetite=self.appetite)
            )
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(
            self, name: str, is_hungry: bool = True
    ) -> None:

        super().__init__(name, is_hungry)
        self.appetite = 3
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self, name: str, is_hungry: bool = True
    ) -> None:

        super().__init__(name, is_hungry)
        self.appetite = 7
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum([animal.feed() for animal in animals])
