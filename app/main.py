class Animal:
    hungry_animals = []

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        if is_hungry:
            Animal.hungry_animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None | int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            if self in Animal.hungry_animals:
                Animal.hungry_animals.remove(self)
            return self.appetite
        else:
            return 0

    @staticmethod
    def add_to_hungry(animal: list) -> None:
        Animal.hungry_animals.append(animal)


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(hungry_animals: list) -> None:
    needed_food = 0

    for hungry_animal in hungry_animals:
        needed_food += hungry_animal.feed()

    return needed_food
