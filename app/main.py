class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        """Imprime uma saudação com o nome do animal."""
        print(f"Hello, I'm {self.name}")

    def feed(self):
        """
        Alimenta o animal se ele estiver com fome, atualiza seu estado
        e retorna a quantidade de comida consumida.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self):
        """Executa a ação de caçar um rato."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self):
        """Executa a ação de trazer os chinelos."""
        print("The slippers delivered!")


def feed_animals(animals: list):
    """
    Alimenta uma lista de animais e retorna o total de comida consumida.
    """
    return sum(animal.feed() for animal in animals)


# Bloco de execução principal para demonstração e verificação
if __name__ == "__main__":
    print("--- Demonstração da Classe Animal ---")
    lion = Animal("Lion", 25)
    lion.print_name()
    food_points = lion.feed()
    print(f"Food points eaten: {food_points}")
    print(f"Is the lion hungry now? {lion.is_hungry}")
    print(f"Trying to feed the lion again: {lion.feed()}")
    print("-" * 20)

    print("--- Demonstração da Classe Cat ---")
    cat1 = Cat("Cat")
    cat1.print_name()
    cat1.feed()
    cat2 = Cat("Cat2", is_hungry=False)
    print(f"Feeding a non-hungry cat: {cat2.feed()}")
    cat2.catch_mouse()
    print("-" * 20)

    print("--- Demonstração da Classe Dog ---")
    dog1 = Dog("Dog")
    dog1.print_name()
    dog1.feed()
    dog2 = Dog("Dog2", is_hungry=False)
    print(f"Feeding a non-hungry dog: {dog2.feed()}")
    dog2.bring_slippers()
    print("-" * 20)

    print("--- Demonstração da Função feed_animals ---")
    # Conforme o exemplo: cat está satisfeito, lion e dog estão com fome.
    cat_for_list = Cat("ListCat", is_hungry=False)
    lion_for_list = Animal("ListLion", 25, True)
    dog_for_list = Dog("ListDog")

    animal_list = [cat_for_list, lion_for_list, dog_for_list]
    total_eaten = feed_animals(animal_list)
    print(f"\nTotal food points needed for the list: {total_eaten}")
    print(f"Expected result: 32. Matches: {total_eaten == 32}")
    print("-" * 20)
