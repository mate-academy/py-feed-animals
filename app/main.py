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
        food_point = 0
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            food_point = self.appetite
        return food_point


class Cat(Animal):

    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
            appetite: int = 3
    ) -> None:
        super().__init__(name, appetite, is_hungry)
        self.appetite = 3

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True, appetite: int = 7) -> None:
        # self.appetite = 7
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals_list: list[Animal]) -> int:
    food_sum = 0
    for animal in animals_list:
        food_sum += animal.feed()
    return food_sum
