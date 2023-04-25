from app.animals.animal import Animal


def feed_animals(animals: list[Animal]) -> int:
    sum_of_food_points = 0
    for animal in animals:
        sum_of_food_points += animal.feed()
    return sum_of_food_points
