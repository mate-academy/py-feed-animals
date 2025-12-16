from app.animal.base.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


if __name__ == "__main__":
    dog = Dog("Dog")
    dog.print_name()
    dog.feed()
    dog.bring_slippers()
