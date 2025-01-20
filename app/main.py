from typing import Any


class Animal:
    def __init__(
        self,
        name: str,
        appetite: int,
        is_hungry: bool = True
    ) -> None:
        self.name : str = name
        self.appetite : int = appetite
        self.is_hungry : bool = is_hungry

    def feed(self, food: Any = None) -> Any:
        if self.is_hungry:
            if food is None:
                print(f"Eating {self.appetite} food points...")
                self.is_hungry = False
                return self.appetite

        return 0

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")


class Cat(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list["Animal"]) -> int:
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food


# lion = Animal("Lion", 25)
# lion.print_name()  # "Hello, I'm Lion"
# food_points = lion.feed()  # "Eating 25 food points..."
# print(food_points)  # 25
# print(lion.is_hungry)  # False
# print(lion.feed())  # 0


# cat = Cat("Cat")
# cat.print_name()  # "Hello, I'm Cat"
# cat.feed()  # "Eating 3 food points"
# cat2 = Cat("Cat", False)
# print(cat2.feed())  # 0
# cat2.catch_mouse()  # "The hunt began!"

# dog = Dog("Dog")
# dog.print_name()  # "Hello, I'm Dog"
# dog.feed()  # "Eating 7 food points"

# dog2 = Dog("Dog", False)
# print(dog2.feed())  # 0
# dog2.bring_slippers()  # "The slippers delivered!"

# cat = Cat("Cat", False)
# lion = Animal("Lion", 25, True)
# dog = Dog("Dog")
# print(feed_animals([cat, lion, dog]) == 32)
