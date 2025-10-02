""""
Description: A class to manage Chequing Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount


class ChequingAccount(BankAccount):
    """
    Chequing Account class: Maintains chequing account item data.
    """

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date, overdraft_limit: float,
                 overdraft_rate: float):
        """
        Initializes class attributes to argument values.

        Args:
            - overdraft_limit(float): The maximum amount a balance can 
            be overdrawn (below 0.00) before overdraft fees are 
            applied.
            - overdraft_rate(float): The rate to which overdraft fees 
            will be applied.
            - account_number(int):  An integer value representing the 
            bank account number.
            - client_number(int):  An integer value representing the 
            client number representing the account holder.
            - balance(float): A float value representing the current 
            balance of the bank account.
            # date_created(date): Date representing the date created.
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05


    def __str__(self) -> str:
        """
        Returns a string representation of the Chequing Account class
        instance.

        Returns:
            str: The Chequing Account instance formatted as a string.
        """
        bank_account_string = super().__str__()
        chequing_account_string = ("\nOverdraft Limit: "
                            + f"${self.__overdraft_limit} Overdraft Rate: "
                            + f"{self.__overdraft_rate}% Account Type: "
                            + "Chequing")

        return (bank_account_string + chequing_account_string)


    def get_service_charges(self) -> float:
        """
        Simulates the get service charges process according to the 
        overdraft limit and overdraft rate.

        """

        if self.balance >= self.__overdraft_limit:
            self.__overdraft_limit = super().BASE_SERVICE_CHARGE

        else:
            self.__overdraft_limit = super().BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
