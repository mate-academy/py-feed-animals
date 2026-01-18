class Animal:

    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        return print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.is_hungry:
            return 0
        else:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        return print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        return print("The slippers delivered!")


def feed_animals(list_of_animals: list[Animal]) -> int:
    result_point = 0
    for animal in list_of_animals:
        result_point += animal.feed()
    return result_point
