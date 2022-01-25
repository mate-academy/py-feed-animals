class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        print(f"Eating {self.appetite} food points...")
        if self.is_hungry is True:
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):

    def __init__(self, name, is_hungry=True):
        super(Cat, self).__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name, is_hungry=True):
        super(Dog, self).__init__(name, 7, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


def feed_animals(lst):
    count = 0
    for beast in lst:
        if beast.is_hungry is True:
            count += beast.appetite
    return count

# cat = Cat("Cat", False)
# lion = Animal("Lion", 25, True)
# dog = Dog("Dog")
# print(feed_animals([cat, lion, dog]))
