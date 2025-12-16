#  write your code here
from app.animal.base.animal import Animal
from app.animal.dog import Dog
from app.animal.cat import Cat


def feed_animals(animals: list[Animal]) -> int:
    return sum([animal.feed() for animal in animals if animal.is_hungry])


if __name__ == "__main__":
    cat = Cat("Cat", False)
    lion = Animal("Lion", 25, True)
    dog = Dog("Dog")
    print(feed_animals([cat, lion, dog]) == 32)
