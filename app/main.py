class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        elif self.is_hungry is False:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True,
                 appetite: int = 3) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True,
                 appetite: int = 7) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(list_animals: list) -> int:
    feed_anima = 0
    for feed_anim in list_animals:
        feed_anima = feed_anima + feed_anim.feed()
    return feed_anima
