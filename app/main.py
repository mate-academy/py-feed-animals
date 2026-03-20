class Animal:
    def __init__(
            self,
            name: str,
            appetite: str,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.apetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.apetite} food points...")
            self.is_hungry = False
            return self.apetite
        self.apetite = 0
        return self.apetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=True)
        self.name = name
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=True)
        self.name = name
        self.is_hungry = is_hungry

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(list_of_animals: list) -> int:
    return sum(animal.feed() for animal in list_of_animals)
