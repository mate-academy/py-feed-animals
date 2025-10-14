class Animal:
    def __init__(self, name, appetite, is_hungry=True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I am {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} units of food...")
            self.is_hungry = False
        else:
            return 0
    
    class Cat(Animal):
        def __init__(self, name, is_hungry=True) -> None:
            super().__init__(name, appetite=3, is_hungry=is_hungry)
        
        @staticmethod
        def catch_mouse() -> None:
            print("The hunt began!")
    
    class Dog(Animal):
        def __init__(self, name, is_hungry=True) -> None:
            super().__init__(name, appetite=7, is_hungry=is_hungry)

        @staticmethod
        def bring_slippers() -> None:
            print("The slippers delivered!")

    def feed_animals(animals: list) -> int:
        total_food = 0
        for animal in animals:
            food = animal.feed()
            total_food += food if food else 0
        return total_food
