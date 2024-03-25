class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

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
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    result = 0
    for animal in animals:
        if animal.is_hungry:
            animal.feed()
            result += animal.appetite
    return result


cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")
feed_animals([cat, lion, dog])


"""
def feed_animals(animals: list) -> int:
    total_food_points = 0
    for animal in animals:
        food_points = animal.feed()
        total_food_points += food_points
    return total_food_points
"""