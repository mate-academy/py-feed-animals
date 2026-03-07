from app.foodAnimal.animals import Animal


class Cat(Animal):
    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")
