class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.appetite > 0 and self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite

        else:
            self.appetite = 0
            print(self.appetite)


lion = Animal("Lion", 25)
lion.print_name()
food_points = lion.feed()  # "Eating 25 food points..."
print(food_points)
print(lion.is_hungry)
print(lion.feed())