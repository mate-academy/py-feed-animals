class Animal:

    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.appetite > 0 and self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            result = self.appetite
            self.appetite = 0
        else:
            result = 0
        return result


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    result = 0
    for animal in animals:
        if animal.appetite > 0 and animal.is_hungry is True:
            result += animal.appetite
            animal.feed()
    return result
