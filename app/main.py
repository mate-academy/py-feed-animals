class Animal:
    def __init__(
            self,
            name: str,
            apetite: int,
            is_hungry: bool = True
    ) -> None:

        self.name = name
        self.apetite = apetite
        self.is_hungry = is_hungry


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)
        self.name = name
        self.is_hungry = is_hungry


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)
        self.name = name
        self.is_hungry = is_hungry
