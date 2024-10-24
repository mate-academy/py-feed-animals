class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        print(f"Eating {self.appetite} food points...")
        if self.is_hungry:
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name, appetite=7)
        self.is_hungry = is_hungry

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    sum_food_points = 0
    for animal in animals:
        sum_food_points += animal.feed()
    return sum_food_points


lion = Animal("Lion", 25)
lion.print_name()  # "Hello, I'm Lion"
food_points = lion.feed()  # "Eating 25 food points..."
print(food_points)  # 25
print(lion.is_hungry)  # False
print(lion.feed())  # 0

cat = Cat("Cat")
cat.print_name()  # "Hello, I'm Cat"
cat.feed()  # "Eating 3 food points"

cat2 = Cat("Cat", False)
print(cat2.feed())  # 0
cat2.catch_mouse()  # "The hunt began!"

dog = Dog("Dog")
dog.print_name()  # "Hello, I'm Dog"
dog.feed()  # "Eating 7 food points"

dog2 = Dog("Dog", False)
print(dog2.feed())  # 0
dog2.bring_slippers()  # "The slippers delivered!"

cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")
assert feed_animals([cat, lion, dog]) == 32
