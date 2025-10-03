""""
Description: A class to manage Savings Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    Savings Account class: Maintains savings account item data.
    """
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date, minimum_balance: float):
        """
        Initializes class attributes to argument values.

        Args:
            - account_number(int):  An integer value representing the 
            bank account number.
            - client_number(int):  An integer value representing the 
            client number representing the account holder.
            - balance(float): A float value representing the current 
            balance of the bank account.
            # date_created(date): Date representing the date created.
            - minimum_balance (float): A float representing the minimum
            account balance.
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0
