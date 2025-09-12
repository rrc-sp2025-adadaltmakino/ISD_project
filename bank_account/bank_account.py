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

        """
