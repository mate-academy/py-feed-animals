from app.animal import Animal, Cat, Dog


def feed_animals(ls_animals: list[Animal | Cat | Dog]) -> int:
    feed_points = 0
    for animal in ls_animals:
        feed_points += animal.feed()

    return feed_points
