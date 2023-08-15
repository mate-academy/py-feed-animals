if __name__ == "__main__":
    from animals import Animal, Cat, Dog
else:
    from .animals import Animal, Cat, Dog


# Function which takes a list of animals.
# It should feed passed animals and return a sum of food points
# that are needed to feed all hungry animals from this list.
def feed_animals(animals_list: list) -> int:
    feed = 0
    for animal in animals_list:
        feed += animal.feed()
    return feed


# Control check function
if __name__ == "__main__":
    lion = Animal("Lion", 25, True)
    cat = Cat("Cat", False)
    dog = Dog("Dog")
    print(feed_animals([cat, lion, dog]))  # 32

    dog.print_name()  # "Hello, I'm Dog"
    dog.feed()  # "Eating 7 food points"

    dog2 = Dog("Dog", False)
    print(dog2.feed())  # 0
    dog2.bring_slippers()  # "The slippers delivered!"
