from typing import List


# --------------------------------------------
# DEFINICJA KLASY BAZOWEJ
# --------------------------------------------
# Kazde zwierze ma ime apetyt (pkt jedzenia) i stan glodu

class Animal:

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry:
            bool = True
    ) -> None:
        self.name = name                    # nazwa zwierzaka
        self.appetite = appetite            # ile pkt apetytu potrzebuje
        self.is_hungry = is_hungry          # czy jest glodne domysle TRUE

    def print_name(self) -> None:
        # wypisuje imei zwierzaka
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        # karmienie jesli jest glodne
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


# ----------------------------
# Definicja klasy Cat (dziedziczy po Animal)
# ----------------------------
# Koty zawsze mają apetyt 3 i dodatkową metodę catch_mouse

class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        # wywolanie konstruktora klasy bazowej apety sztywno na 3
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        # metoda specjalna dla kota
        print("The hunt began!")
# cat1 = Cat("Filemon")
# cat1.print_name()
# cat1.feed()
# cat1.catch_mouse()


# ----------------------------
# Definicja klasy Dog (dziedziczy po Animal)
# ----------------------------
# Psy zawsze mają apetyt 7 i dodatkową metodę bring_slippers
class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        # Wywołanie konstruktora klasy bazowej z sztywnym apetytem = 7
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        # Specjalna metoda dla psa
        print("The slippers delivered!")

# dog1 = Dog("Reksio")
# dog1.print_name()
# dog1.feed()
# dog1.bring_slippers()
#
# dog2 = Dog("Fafik", False)
# dog2.print_name()
# dog2.feed()
# dog2.bring_slippers()

# ----------------------------
# Funkcja feed_animals
# ----------------------------
# Karmienie wielu zwierząt na raz
# Przyjmuje listę obiektów zwierząt
# Zwraca sumę punktów jedzenia faktycznie zjedzonych przez głodne zwierzęta


def feed_animals(animals_list: List[Animal]) -> None:
    total_food = 0
    for animal in animals_list:
        total_food += animal.feed()
    return total_food

# cat = Cat("Filemon", False)
# lion = Animal("Lion", 25, True)
# dog = Dog("Reksio")
#
# print(feed_animals([cat, lion, dog]))
