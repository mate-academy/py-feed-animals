from app.classes.animal import Animal
from app.classes.cat import Cat
from app.classes.dog import Dog


def feed_animals(animals: list[Animal | Cat | Dog]) -> int:
    food_needed = 0
    for animal in animals:
        food_needed += animal.feed()
    return food_needed
