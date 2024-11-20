from app.animals.animal import Animal # noqa
from app.animals.dog import Dog # noqa
from app.animals.cat import Cat # noqa


def feed_animals(animals: list) -> int:
    return sum(animal.feed() for animal in animals)
