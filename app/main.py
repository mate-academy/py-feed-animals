class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(animal_list: list[Animal]) -> int:
    feed = []
    for animal in animal_list:
        feed.append(animal.feed())
    return sum(feed)
