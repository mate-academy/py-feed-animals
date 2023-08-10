class Animal:

    def __init__(self,
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
        eating_points = 0
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            eating_points += self.appetite
        return eating_points


class Cat(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(hungry_animals: list[Animal]) -> int:
    food_points = 0
    for animal in hungry_animals:
        food_points += animal.feed()
    return food_points
