class Animal:

    def __init__(self, name: str,
                       appetite: int, 
                       is_hungry: bool=True) ->None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        
    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self):
        print("The hunt began!")

class Dog(Animal):
    def __init__(self,
                 name: str, appetite: int=7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")

