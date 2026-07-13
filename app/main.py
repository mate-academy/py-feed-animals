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

    def feed(self) -> int:

        if self.is_hungry:
            self.is_hungry = not self.is_hungry
            self.appetite = 0
            print(f"Eating {self.appetite} food points...")
            return self.appetite

        return 0

class Cat(Animal):

    def __init__(self, name: str, is_hungry: bool = True):
        super().__init__(self.name, 3, self.is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


