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
        """Imprime o nome usando f-string e aspas duplas."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Alimenta o animal se ele estiver com fome.
        Não utiliza o bloco 'else' conforme a regra de eficiência.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite

        return 0


class Cat(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        """Gatos sempre têm apetite igual a 3."""
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        """Imprime a mensagem de caça."""
        print("The hunt began!")


class Dog(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        """Cães sempre têm apetite igual a 7."""
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        """Imprime a mensagem de entrega."""
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    """
    Calcula o total de pontos de comida usando uma expressão geradora.
    """
    return sum(animal.feed() for animal in animals)
