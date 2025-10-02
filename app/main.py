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

    def feed(self):
        if self.appetite > 0:
            print(f"Eating {self.appetite} food points...")
            eaten_points = self.appetite
            self.appetite = 0
            self.is_hungry = False
            return eaten_points

        return self.appetite

class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool) -> None:
        super().__init__(name, 3, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")
