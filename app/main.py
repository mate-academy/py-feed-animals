class Animal:
    animal_list = []

    def __init__(
            self, name: str, appetite: int, is_hungry: bool = True
    ) -> any:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animal_list.append(self)

    def print_name(self) -> any:
        return print(f"Hello, I'm {self.name}")

    def feed(self) -> any:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> any:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> any:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> any:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> any:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    result = 0
    for animal in animals:
        result += animal.feed()
    return result
