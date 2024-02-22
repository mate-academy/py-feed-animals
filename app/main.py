class Animal:

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True,
    ) -> None:

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:

        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            points = self.appetite
        else:
            points = 0

        self.is_hungry = False

        return points


class Cat(Animal):

    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:

        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")
        pass


class Dog(Animal):

    def __init__(self, name: str,
                 is_hungry: bool = True
                 ) -> None:

        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")
        pass


def feed_animals(lst: list) -> int:
    total_amount = 0

    for animal in lst:

        total_amount += animal.feed()

    return total_amount


dog = Dog("Dog", False)
dog.print_name()
dog.feed()
