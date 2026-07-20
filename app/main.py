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
        # print(f"Eating {self.appetite} food points...")
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            self.appetite = 0
            return self.appetite


class Cat(Animal):
    def __init__(self, name: str,
                 is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str,
                 is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(list_animals: list) -> int:
    count_feed = 0
    for animal in list_animals:
        if animal.is_hungry:
            count_feed += animal.appetite
            animal.feed()
    return count_feed
