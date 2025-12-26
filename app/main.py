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
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:

        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:

        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(list_animals: list) -> int:
    return sum(animal.feed() for animal in list_animals)
    # result = 0
    # for animal in list_animals:
    #     if animal.is_hungry:
    #         potion = animal.feed()
    #         result += potion
    #
    #         if potion == 0:
    #             if isinstance(animal, Cat):
    #                 animal.catch_mouse()
    #             elif isinstance(animal, Dog):
    #                 animal.bring_slippers()
    #
    # return result
