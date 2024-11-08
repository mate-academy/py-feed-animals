class Animal:
    """
    Class which contains animals. It stores list of in animals list.
    """
    animals = []

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: type(bool) = True) -> None:
        """
        Create instance of Animal.
        :param name: animal's name.
        :param is_hungry: boolean that shows if animal is ready to eat
        with True default value.
        :param appetite: integer that shows how much food points.
        this animal need to eat to be full.

        """
        self.name = name
        self.is_hungry = is_hungry
        self.appetite = appetite
        Animal.animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Function that feed animal if it's is_hungry equal True.
        It prints how many food points animal ate, return
        value of animal's appetite and change is_hungry to False.
        If animal is_hungry is equal to False, function return 0.
        :return:
        """
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3)
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name : str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7)
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals_list: list[Animal]) -> int:
    """
    Feed every animal from a list using Animal.feed().
    :param animals_list: list of Animal instances.
    :return: sum of food points needed to feed all animals
    from a list.
    """
    new_result = sum([animal.appetite for animal
                      in animals_list if animal.is_hungry is True])
    result = []
    if len(animals_list) > 1:
        for animal in animals_list:
            if animal.is_hungry is True:
                result.append(animal.appetite)
                animal.feed()
    if len(animals_list) <= 1:
        animals_list[0].feed()
    return new_result
