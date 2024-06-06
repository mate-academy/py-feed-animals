class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    @staticmethod
    def print_name() -> None:
        print("Hello, I'm {self.name}")

    def feed(self) -> None:
        if self.is_hungry is False:
            return None
        if self.is_hungry is True:
            print("Eating {self.appetite} food points.")

    def feed_animals(self):
        total_food_points = 0
        for animal in animals:
            total_food_points += animal.feed()
        return total_food_points

 class Cat(Animal):
        def __init__(self, name: str, is_hungry = True, appetite = 3):
            super().__init__()
            self.name = name
            self.is_hungry = is_hungry
            self.appetite = appetite

        @staticmethod
        def catch_mouse() -> None:
            print("The hunt began!")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bring_slippers(self):
        print("The slippers delivered!")








