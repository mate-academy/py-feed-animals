class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        return f"Hello, I'm {self.name}"

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, appetite: int = 3, is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)
        self.appetite = appetite
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, appetite: int = 7, is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)
        self.appetite = appetite
        self.is_hungry = is_hungry

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    feed_num = []
    for animal in animals:
        feed_num.append(animal.feed())
    return sum(feed_num)

cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")

print(feed_animals([cat, lion, dog]))