class Animal:
    animal_list = []

    def __init__(self,
                 name: str, appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animal_list.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super(). __init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(animal_list: list) -> list:
    sum_result = sum(animal.feed() for animal in animal_list)
    return sum_result


cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")
print(feed_animals([cat, lion, dog]))
