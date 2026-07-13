class Animal:

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

