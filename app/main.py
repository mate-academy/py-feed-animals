#  write your code here
class Animal:
    def __init__(self
                 , name: str
                 , appetite: int
                 , is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self
                 , name: str
                 , appetite: int = 3
                 , is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self
                 , name: str
                 , appetite: int = 7
                 , is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> None:
    total_feel = 0
    for animal in animals:
        if animal.is_hungry:
            total_feel += animal.feed()
    return total_feel
