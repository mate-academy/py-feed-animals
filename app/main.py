from app.animal import Animal, Cat, Dog


def feed_animals(ls_animals: list[Animal | Cat | Dog]) -> int:
    return sum([animal.feed() for animal in ls_animals])
