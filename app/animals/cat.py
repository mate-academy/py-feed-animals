from app.animals.animal import Animal


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
    ) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")
