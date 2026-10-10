from app.classes.animal import Animal
from app.classes.cat import Cat
from app.classes.dog import Dog


def feed_animals(animals: list[Animal | Cat | Dog]) -> int:
    return sum(animal.feed() for animal in animals)
