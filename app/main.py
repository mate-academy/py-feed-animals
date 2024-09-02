class Animal:
    list_animals = []

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

        Animal.list_animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if not self.is_hungry:
            self.appetite = 0
            return self.appetite
        print(f"Eating {self.appetite} food points...")
        self.is_hungry = False
        return self.appetite


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True
                 ) -> None:

        super().__init__(name, appetite, is_hungry)

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True
                 ) -> None:

        super().__init__(name, appetite, is_hungry)

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animal: list) -> int:
    food_count = 0
    for food in animal:
        food_count += Animal.feed(food)
    return food_count
