class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
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
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food


lion = Animal("Lion", 25)
lion.print_name()
food_points = lion.feed()
print(food_points)
print(lion.is_hungry)
print(lion.feed())

cat = Cat("Cat")
cat.print_name()
cat.feed()

cat2 = Cat("Cat", False)
print(cat2.feed())
cat2.catch_mouse()

dog = Dog("Dog")
dog.print_name()
dog.feed()

dog2 = Dog("Dog", False)
print(dog2.feed())
dog2.bring_slippers()

print(feed_animals([cat2, lion, dog]))
