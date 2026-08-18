# Extracted  3 / 7 into module-level constants instead of class-level
# because there is the tests that chek if classes have only 1 method
#       AssertionError: Only one method 'bring_slippers' should be
#           defined inside class 'Dog' except '__init__'
#           assert 3 == 2
CAT_APPETITE = 3
DOG_APPETITE = 7


class Animal:
    def __init__(self, name: str,
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


class Cat(Animal):

    def __init__(self, name: str,
                 is_hungry: bool = True) -> None:
        super().__init__(name, CAT_APPETITE, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 is_hungry: bool = True) -> None:
        super().__init__(name, DOG_APPETITE, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food
