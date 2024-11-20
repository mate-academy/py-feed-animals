class Animal:

    def __init__(self,
                 name: str,
                 appetite: int = 0,
                 is_hungry: bool = True) -> None:

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.appetite == 0 or not self.is_hungry:
            self.appetite = 0
            return self.appetite
        else:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:

        super().__init__(name, is_hungry)
        self.appetite = appetite
        if not self.appetite:
            self.appetite = 0

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:

        super().__init__(name, is_hungry)
        self.appetite = appetite
        if not self.appetite:
            self.appetite = 0

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    result = 0
    for animal in animals:
        result += animal.feed()
    return result
