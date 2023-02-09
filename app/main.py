#  write your code here
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
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @classmethod
    def catch_mouse(cls) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @classmethod
    def bring_slippers(cls) -> str:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list) -> int:
    summ = 0
    for animal in list_of_animals:
        if animal.is_hungry is True:
            animal.feed()
            summ += animal.appetite
    return summ
