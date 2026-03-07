#  write your code here
from app.foodAnimal.animals import Animal


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
