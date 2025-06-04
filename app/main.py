from typing import List
# # Feed animals
#
# **Please note:** read [the guideline]
# (https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
# before starting.
#
# All animals love delicious food. Let's create a new class to feed them.
# Create class `Animal` which `__init__` method takes three arguments:
# * `name` - the animal name
# * `appetite` - an integer that shows
# how much *food points* this animal need to eat to be full.
# * `is_hungry` - boolean that shows
# if animal is ready to eat with `True` default value.


class Animal:
    def __init__(self, name: str, appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
    # `Animal` should have two methods:
    # * `print_name` - should print
    # name in the following format: `Hello, I'm {name}`

    def print_name(self):
        print(f"Hello, I'm {self.name}")
    # * `feed` - should print `Eating {appetite} food points...`,

    def feed(self):

        # set `is_hungry` to `False` and return
        # number of eaten food points if animal is hungry.
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite

        # Otherwise, it should return 0 and print nothing.
        else:
            return 0

# Example:
# ```python
# lion = Animal("Lion", 25)
# lion.print_name()  # "Hello, I'm Lion"
# food_points = lion.feed()  # "Eating 25 food points..."
# print(food_points)  # 25
# print(lion.is_hungry)  # False
# print(lion.feed())  # 0
# ```
#
# There is a well-known fact that all cats eat 3 food points at a time.
# Also, they can catch a mouse.
# Write `Cat` class which is a child of `Animal`.


class Cat(Animal):
    # It should have the `__init__` method with two arguments:
    # * `name` - the name of a cat
    # * `is_hungry` - with `True` default value
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)
    # Note: you need call the super
    # class `__init__` method with `appetite` equal to 3.
    #
    # `Cat` should have only one
    # additional method `catch_mouse` which should print
    # `The hunt began!`

    def catch_mouse(self):
        print("The hunt began!")

# Example:
# ```python
# cat = Cat("Cat")
# cat.print_name()  # "Hello, I'm Cat"
# cat.feed()  # "Eating 3 food points"
#
# cat2 = Cat("Cat", False)
# print(cat2.feed())  # 0
# cat2.catch_mouse()  # "The hunt began!"
# ```
#
# The last class you should implement is a `Dog` class.
# Its `__init__` method should have two arguments:
# * `name` - the name of a dog
# * `is_hungry` - with `True` default value


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)
    # All dogs should have `appetite` equal to 7.
    #
    # `Dog` should have one additional
    # method `bring_slippers` that should print
    # `The slippers delivered!`

    def bring_slippers(self):

        print("The slippers delivered!")
# Example:
# ```python
# dog = Dog("Dog")
# dog.print_name()  # "Hello, I'm Dog"
# dog.feed()  # "Eating 7 food points"
#
# dog2 = Dog("Dog", False)
# print(dog2.feed())  # 0
# dog2.bring_slippers()  # "The slippers delivered!"
# ```
#
# Now, it's time to feed many animals at a time.
# Implement `feed_animals` function which takes a list of animals.
# It should feed passed animals
# and return a sum of food points that are needed to feed all hungry
# animals from this list.


def feed_animals(animals: List[Animal]):

    feed_points = 0
    for animal in animals:
        feed_points += animal.feed()
    return feed_points

# Example:
# ```python
# cat = Cat("Cat", False)
# lion = Animal("Lion", 25, True)
# dog = Dog("Dog")
# feed_animals([cat, lion, dog]) == 32
# ```
#
# ### Note: Check your code using this
# [checklist](checklist.md) before pushing your solution.
