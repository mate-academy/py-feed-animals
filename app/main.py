class Animal:
    alive = []

    def __init__(self, name: str,
                 appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        self.health = 100  # Default health for all animals
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Appetite: {self.appetite}, "
                f"Is Hungry: {self.is_hungry}, Health: {self.health}}}")

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not getattr(self, "hidden", False)


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if (isinstance(herbivore, Herbivore)
                and not getattr(herbivore, "hidden", False)):
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.health = 0
                Animal.remove_dead()


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    total_food = 0
    for animal in animals:
        total_food += animal.feed()
    return total_food
