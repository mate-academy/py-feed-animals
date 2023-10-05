from app.animals.animals import Animal


def feed_animals(animals: list) -> int:
    total_food_points = 0
    for animal in animals:
        total_food_points += Animal.feed(animal)
    return total_food_points
