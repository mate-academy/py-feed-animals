from app.animal import Animal, Cat, Dog


def feed_animals(animals: list[Animal | Cat | Dog]) -> int:
    return sum(animal.feed() for animal in animals)
