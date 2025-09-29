""""
Description: A class to manage Chequing Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    Chequing Account class: Maintains chequing account item data.
    """

    def __init__(self, overdraft_limit:float, overdraft_rate:float,
                 BASE_SERVICE_CHARGE: float, account_number:int, 
                 client_number:int, balance:float, date_created:date):
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

        super().__init__(BASE_SERVICE_CHARGE, account_number, client_number,
                         balance, date_created)

        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit
        else:
            raise ValueError ("")



    def __str__(self) -> str:
        """
        
        """
        return

    def get_service_charges(self) -> float:
        """
        
        """
