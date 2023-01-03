from app.program_files.animals import Cat, Dog
from app.program_files.alimal import Animal


def feed_animals(animals: list[Animal, Cat, Dog]) -> int:
    res = 0
    for animal in animals:
        if animal.is_hungry:
            animal.feed()
            res += animal.appetite
    return res
