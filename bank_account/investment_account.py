""""
Description: A class to manage Investment Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Maintains investment account data.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days = (10 * 365.25))

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
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55


    def __str__(self):
        """
        Returns a string representation of the InvestmentAccount class
        instance.

        Returns:
            str: The Investment Account instance formatted as a string.
        """
        bank_account_string = super().__str__()

        if self._date_created <= InvestmentAccount.TEN_YEARS_AGO:
            management_fee_string = "Waived"
        else:
            management_fee_string = f"${self.__management_fee:,.2f}"

        investment_account_string = (f"Date Created: {self._date_created} "
                                + f"Management Fee: {management_fee_string} "
                                + "Account Type: Investment")

        return (bank_account_string + investment_account_string)


    def get_service_charges(self):
        """
        Simulates the get service charges process according to the 
        balance, overdraft limit, and overdraft rate.

        Returns:
            float: The calculated service rate.
        """

        if self._date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
