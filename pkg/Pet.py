from .Animal import Animal

class Pet(Animal):
    def __init__(self, name, age) -> None:
        
        """
        Initialize a Pet with optional name and age.

        Args:
            name (str, optional): The name of the pet.
            age (int, optional): The age of the pet.

        Returns:
            None
        """

        self.name = name
        self.age = age
        pass

    # Name property

    @property
    def name(self) -> str:
        
        """
        Get the name of the pet.

        Returns:
            str: The name of the pet.
        """

        input("What is the name of your Pet?")
        return self.name

    @name.setter
    def name(self, value: str) -> None:
        """
        Set the name of the pet.

        Args:
            value (str): The name to be set.

        Returns:
            None
        """
        self.name = value
        pass

    # Age property

    @property
    def age(self) -> int:
        """
        Get the age of the pet.

        Returns:
            int: The age of the pet.
        """
        return -1

    @age.setter
    def age(self, value: int) -> None:
        """
        Set the age of the pet.

        Args:
            value (int): The age to be set.

        Returns:
            None
        """
        pass

    # Owner property

    @property
    def owner(self):
        """
        Get the owner of the pet.

        Returns:
            PetOwner: The owner of the pet.
        """
        return None

    @owner.setter
    def owner(self, value) -> None:
        """
        Set the owner of the pet.

        Args:
            value (PetOwner): The owner to be set.

        Returns:
            None
        """
        pass

    def __str__(self) -> str:
        """
        Get a string representation of the pet.

        Returns:
            str: A string representing the pet.
        """
        return ""
