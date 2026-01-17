class Animal:
    """
    Represents an animal with a name, appetite, and
    hunger status.

    This class allows handling of basic animal attributes
    and provides functionality
    to feed the animal or print its name.

    :ivar name: Name of the animal.
    :type name: str
    :ivar appetite: Amount of food the animal can consume.
    :type appetite: int
    :ivar is_hungry: Indicates if the animal is currently
        hungry. Defaults to True.
    :type is_hungry: bool
    """

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        """
        Represents an animal with a name, an appetite level,
        and a hunger state.

        This class models basic attributes for an animal,
        including its name, appetite measure, and whether
        it is currently hungry. It can serve as the
        foundation for more specific animal classes or behavior models.

        :param name: The name of the animal.
        :type name: str
        :param appetite: The numerical value indicating the
            animal's appetite level.
        :type appetite: int
        :param is_hungry: A boolean flag indicating whether
            the animal is currently hungry. Defaults to True.
        :type is_hungry: bool
        """
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """
        Prints the name of the instance in a
        formatted message.

        This method displays a greeting message that
        includes the instance's `name` attribute. Use this
        function to confirm or display the
        `name` set for the object.

        :return: None
        """
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """
        Feeds the entity if it is hungry. If the entity
        is hungry, it consumes food pointsvequal to its
        appetite and updates its hunger status.

        :return: The amount of food points consumed when
        the entity is fed, or 0 if it
            is not hungry.
        :rtype: int
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        """
        Initiates the mouse-catching action and
        displays a message indicating the start of the hunt.

        This method signifies the beginning of a
        specific action where the instance is involved in catching
        a mouse. No arguments are accepted or returned.
        The output is a printed notification.

        :return: None
        """
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """
        Initializes a new instance of the class,
        setting up the essential attributes.

        :param name: Name of the instance.
        :type name: str
        :param is_hungry: Indicates whether the
        instance is hungry. Defaults to True.
        :type is_hungry: bool
        """
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        """
        The `bring_slippers` method performs an action
        to deliver slippers. This action is executed
        without requiring any input parameters
        and does not return a value.

        :return: None
        """
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    """
    Feeds a list of Animal objects and calculates
    the total food points used.

    This function iterates through a provided list
    of animals, invokes their feed method, and sums
    up the food points consumed. The function helps
    track the total food consumption for the given
    list of animals.

    :param animals: A list of Animal objects to be fed.
    :type animals: list[Animal]
    :return: The total amount of food points consumed
        by all animals.
    :rtype: int
    """
    return sum(animal.feed() for animal in animals)
