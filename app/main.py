from typing import List, Union

from app.animals.animal import Animal
from app.animals.cat import Cat
from app.animals.dog import Dog


def feed_animals(all_animals: List[Union["Animal", "Cat", "Dog"]]) -> int:
    all_food = sum(animal.feed() for animal in all_animals)
    return all_food
