import pytest
from app.main import Animal, Cat, Dog, feed_animals

def test_animal_feed():
    lion = Animal("Lion", 25)
    assert lion.feed() == 25
    assert not lion.is_hungry
    assert lion.feed() == 0

def test_cat_behavior():
    cat = Cat("Cat")
    assert cat.feed() == 3
    assert not cat.is_hungry

    cat2 = Cat("Cat", False)
    assert cat2.feed() == 0

def test_dog_behavior():
    dog = Dog("Dog")
    assert dog.feed() == 7
    assert not dog.is_hungry

    dog2 = Dog("Dog", False)
    assert dog2.feed() == 0

def test_feed_animals():
    cat = Cat("Cat", False)
    lion = Animal("Lion", 25, True)
    dog = Dog("Dog")
    assert feed_animals([cat, lion, dog]) == 32