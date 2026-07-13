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
            self.is_hungry = not self.is_hungry
            appetite_result = self.appetite
            print(f"Eating {appetite_result} food points...")
            self.appetite = 0
            return appetite_result

        return 0

class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")

def feed_animals(animals: list[Animal]) -> int:
    return sum([animal.appetite for animal in animals])