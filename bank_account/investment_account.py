""""
Description: A class to manage Investment Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from datetime import date
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Maintains investment account data.
    """

    TEN_YEARS_AGO: date
    management_fee: float

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, management_fee: float):
        """
        Initializes class attributes to argument values.

        Args:
            account_number(int):  An integer value representing the 
            bank account number.
            client_number(int):  An integer value representing the 
            client number representing the account holder.
            balance(float): A float value representing the current 
            balance of the bank account.
            date_created(date): Date representing the date created.
            management_fee(float):A float value representing the 
            management fee.
        """
        