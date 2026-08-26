class Animal:
    def __init__(self, name: str,
                 appetite : int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        food_points = self.appetite

        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return food_points
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(feed_animal: list[Animal]) -> None:
    count_feed = 0
    for ani in feed_animal:
        count_feed += ani.feed()
    return count_feed
