class Animal:

    def __init__(
            self,
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
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
            self.appetite = 0
        return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3)
        self.name = name
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7)
        self.name = name
        self.is_hungry = is_hungry

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animal_species: list) -> int:
    suma_of_appetite = 0
    for instance_of_animal in animal_species:
        if instance_of_animal.is_hungry:
            suma_of_appetite += instance_of_animal.appetite
            Animal.feed(instance_of_animal)
    return suma_of_appetite
