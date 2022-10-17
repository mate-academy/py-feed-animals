class Animal:

    def __init__(self, name: str,
                       appetite: int, 
                       is_hungry: bool=True) ->None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        
    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            print(f"")
            return 0


class Cat(Animal):

    def __init__(self, name: str,
                 is_hungry: bool=True) -> None:
        super().__init__(name, is_hungry)
        self.appetite =3

    def catch_mouse(self):
        print("The hunt began!")