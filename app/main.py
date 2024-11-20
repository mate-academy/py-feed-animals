class Animal:
    """
    All animals love delicious food. Let's create a new class to feed them.
    Create class Animal which __init__ method takes three arguments:
    name - the animal name
    appetite - an integer that shows how much food points this animal need
    to eat to be full.
    is_hungry - boolean that shows if animal is ready to eat with True default
    value.
    Animal should have two methods:

    print_name - should print name in the following format: Hello, I'm {name}
    feed - should print Eating {appetite} food points..., set is_hungry to
    False and return number of eaten food points if animal is hungry.
    Otherwise, it should return 0 and print nothing.
    """
    def __init__(
            self, name: str,
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
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


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


def feed_animals(animals: list[Animal]) -> int:
    """
    Now, it's time to feed many animals at a time. Implement feed_animals
    function which takes a list of animals. It should feed passed animals
    and return a sum of food points that are needed to feed all hungry
    animals from this list.
    """
    return sum([animal.feed() for animal in animals])
