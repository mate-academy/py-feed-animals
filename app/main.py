from app.animals import Animal, Cat, Dog, feed_animals


if __name__ == "__main__":
    lion = Animal("Lion", 25)
    lion.print_name()
    print(lion.feed())
    print(lion.is_hungry)

    cat = Cat("Kitty")
    cat.print_name()
    cat.catch_mouse()
    print(cat.feed())

    dog = Dog("Rex")
    dog.print_name()
    dog.bring_slippers()
    print(dog.feed())

    animals = [lion, cat, dog]
    print("Total food eaten:", feed_animals(animals))
