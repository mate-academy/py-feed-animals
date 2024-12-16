class Animal:
    def __init__(
            self,
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
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    food_total_points = 0
    for animal in animals:
        food_total_points += animal.feed()
    return food_total_points


lion = Animal("Lion", 25)
print(lion.print_name())  # "Hello, I'm Lion"
food_points = lion.feed()  # "Eating 25 food points..."
print(food_points)  # 25
print(lion.is_hungry)  # False
print(lion.feed())  # 0

cat = Cat("Cat", )
print(cat.print_name())  # "Hello, I'm Cat"
cat.feed()  # "Eating 3 food points"

cat2 = Cat("Cat", False)
print(cat2.feed())  # 0
print(cat2.catch_mouse())  # "The hunt began!"
