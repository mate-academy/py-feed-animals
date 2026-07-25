from app.animals.animal import Animal
from app.animals.cat import Cat
from app.animals.dog import Dog


def feed_animals(animals: list[Animal | Cat | Dog]) -> int:
    total_food = 0

    for animal in animals:
        total_food += animal.feed()

    return total_food
