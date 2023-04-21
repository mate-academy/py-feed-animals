class Animal:
    def __int__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:


    def print_name(self) -> None:
        print(f"Hello, I`m {self.name}")

    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __int__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print(The hunt began!)

class Dog(Animal):
    def __int__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print(The slippers delivered!)

def feed_animals(animals):
    total_food_points = 0
    total_food_points = sum(animal.feed() for animal in animals)
    return total_food_points

