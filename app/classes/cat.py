from app.classes.animal import Animal


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name,
                         appetite,
                         is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")
