#!/usr/bin/python3
"""defining a square"""


class Square:
    """ represents a square

    Attributes:
        ___size (int): size of a side of the square
        ___position (tuple): pos of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square
        Args:
            size (int): size of a side of the square
            position (tuple): pos of the square

        Returns: None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates square's area

        Returns: None
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size

        Returns:
            The square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the square's size

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def my_print(self):
            """Prints square

            Returns:
                None
            """
            if self.__size == 0:
                print()
                return
            for i in range(self.__position[1]):
                print()
            for b in range(self.__size):

