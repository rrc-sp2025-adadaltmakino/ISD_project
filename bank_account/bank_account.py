""""
Description: A class to manage Bank Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"


class BankAccount:
    """
    BankAccount class: 
    """
    def __init__(self, account_number: int, client_number: int,
                 balance: float):
        """
        Initializes class attributes to argument values.

        Args:
            account_number(int):  An integer value representing the 
            bank account number.
            client_number(int):  An integer value representing the 
            client number representing the account holder.
            balance(float): A float value representing the current 
            balance of the bank account.
        
        Raises:
            ValueError: If account number is not an integer, if client
            number is not an integer, and if balance is not a float
            and cannot be transferred to a float.

        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")

        if isinstance (balance, float):
            self.__balance = balance
        else:
            try:
                self.__balance = float(balance)
            except (ValueError, TypeError):
                self.__balance = 0.0

    @property
    def account_number(self) -> int:
        """
        Accessor for the account number attribute.

        Returns:
            int: An integer value representing the 
            client number representing the account holder.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: An integer value representing the client number 
            representing the account holder.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute.

        Returns:
            float: A float value representing the current balance of 
            the bank account
        """
        return self.__balance

