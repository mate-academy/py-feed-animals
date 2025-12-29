from app.animals.animal import Animal


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
    ) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
       print("The slippers delivered!")
