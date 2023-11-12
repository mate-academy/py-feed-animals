from __future__ import annotations


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
    """
    There is a well-known fact that all cats eat 3 food points at a time.
    Also, they can catch a mouse. Write Cat class which is a child of Animal.
    It should have the __init__ method with two arguments:

    name - the name of a cat
    is_hungry - with True default value
    Note: you need call the super class __init__ method with appetite
    equal to 3.

    Cat should have only one additional method catch_mouse which should print
    The hunt began!
    """
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    """
    The last class you should implement is a Dog class. Its __init__ method
    should have two arguments:

    name - the name of a dog
    is_hungry - with True default value
    All dogs should have appetite equal to 7.

    Dog should have one additional method bring_slippers that should print
    The slippers delivered!
    """

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
