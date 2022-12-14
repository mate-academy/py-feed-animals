class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        is_hungry = True

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
        else:
            self.appetite = 0
        return self.appetite


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=True)
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=True)
        self.is_hungry = is_hungry

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    return sum(animal.feed() for animal in animals)


cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")
print(feed_animals([cat, lion, dog])) == 32
