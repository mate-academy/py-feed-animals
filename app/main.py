class Animal:
    """
    Class that represents an animal and its feeding state.

    Attributes:

        name (str): Is the name of te beast.

        appetite (int): Number that represent how much food points this
            animal need to eat to be full.

        is_hungry (bool): Shows if animal is ready to eat with
            True default value.
    """

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(
            self,
    ) -> None:
        """
        Print the animal's name with a greeting.
        """
        print(f"Hello, I'm {self.name}")

    def feed(
        self
    ) -> int:
        """
        Feed the animal if it is hungry.

        Returns:

            int: The number of food points consumed.

            Returns 0 if the animal was already full.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    """
    Child class that represents a cat.

    Attributes:
        name (str): Name of the cat.
        is_hungry (bool): Current status of the cat's hunger.
    """

    def __init__(
        self,
        name: str,
        is_hungry: bool = True
    ) -> None:
        super.__init__(
            name=name,
            appetite=3,
            is_hungry=is_hungry
        )

    def catch_mouse(
        self
    ) -> None:
        """
        Print the start of the hunt.
        """
        print("The hunt began!")
