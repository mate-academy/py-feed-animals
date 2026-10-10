from app.classes.animal import Animal


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name,
                         appetite,
                         is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")
