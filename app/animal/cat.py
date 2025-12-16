from app.animal.base.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


if __name__ == "__main__":
    cat = Cat("Cat")
    cat.print_name()
    cat.feed()
    cat.catch_mouse()
