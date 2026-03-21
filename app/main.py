class Animal:

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        hunger = 0
        if self.appetite and self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            hunger += self.appetite
            self.is_hungry = False
            self.appetite = 0
            return hunger
        else:
            return 0


class Cat(Animal):

    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    result = 0
    for animal in animals:
        if animal.is_hungry:
            result += animal.appetite
            animal.feed()
        else:
            continue
    return result
