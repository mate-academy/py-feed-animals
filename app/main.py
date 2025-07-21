class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(appetite, int):
            raise TypeError("appetite must be an integer")
        if not isinstance(is_hungry, bool):
            raise TypeError("is_hungry must be a boolean")

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
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(is_hungry, bool):
            raise TypeError("is_hungry must be a boolean")

        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(is_hungry, bool):
            raise TypeError("is_hungry must be a boolean")

        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    if not isinstance(animals, list):
        raise TypeError("animals must be a list of Animal instances")
    total_food = 0
    for animal in animals:
        if not isinstance(animal, Animal):
            raise TypeError(
                "All elements in the list must be instances of Animal or its subclasses"
            )
        total_food += animal.feed()
    return total_food
