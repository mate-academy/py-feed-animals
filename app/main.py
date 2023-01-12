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
        print(f"Hello, I`m {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, is_hungry, appetite=3)
        # self.appetite = 3


# lion = Animal("Lion", 25)
# lion.print_name()  # "Hello, I'm Lion"
# food_points = lion.feed()  # "Eating 25 food points..."
# print(food_points)  # 25
# print(lion.is_hungry)  # False
# print(lion.feed())  # 0

cat = Cat("Cat")
cat.print_name()  # "Hello, I'm Cat"
cat.feed()  # "Eating 3 food points"

# cat2 = Cat("Cat", False)
# print(cat2.feed())  # 0
# cat2.catch_mouse()  # "The hunt began!"