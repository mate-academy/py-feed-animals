from __future__ import annotations

from app.animals.animal import Animal
from app.animals.cat import Cat
from app.animals.dog import Dog


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)

cat = Cat("cat")
dog = Dog("dog")