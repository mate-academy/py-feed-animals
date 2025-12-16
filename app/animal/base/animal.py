class Animal:
    def __init__(
        self,
        name: str,
        appetite: int,
        is_hungry: bool = True,
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def feed(self) -> str | int:
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        return 0

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")
