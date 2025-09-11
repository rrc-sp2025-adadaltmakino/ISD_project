""""
Description: A class to manage Client objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Client class: 
    """
    def __init__(self, client_number: int, first_name: str, last_name:
                 str, email_address: str):
        """
        Initializes class attributes to argument values.

        Args:
            client_number(int): The client number of the Client.
            first_name(str): The first name of the Client.
            last_name(str): The last name of the Client.
            email_address(str): The email address of the Client.

        Raises:
            ValueError: When client number is not an integer, when
            first name is blank, when last name is blank.
             
            EmailNotValid: When email address fails to be validated.
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")

        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")

        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")

        try:
            if validate_email(email_address, check_deliverability= False):
                self.__email_address = email_address
            else:
                raise EmailNotValidError
        except EmailNotValidError:
            self.__email_address = f"{email_address}@pixell-river.com"


    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: Number of the client.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Accessor for the first name attribute.

        Returns:
            str: Client's first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Accessor for the last name attribute.

        Returns:
            str: Client's last name.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Accessor for the email address attribute.

        Returns:
            str: Client's email address.
        """
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The course instance formatted as a string.
        """
        return (
            f"{self.__last_name}, {self.__first_name}"
            + f"[{self.__client_number}] - {self.__email_address}"
        )
