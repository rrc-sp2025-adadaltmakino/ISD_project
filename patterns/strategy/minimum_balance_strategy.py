""""
Description: A class to manage MinimumBalanceStrategy class objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    MinimumBalanceStrategy class: Maintains minimum balance strategy 
    data.
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initializes class attributes to argument values.

        Args:
            minimum_balance(float): The minimum account balance.
        """

        self.__minimum_balance = minimum_balance


    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Simulates the get service charges process.

        Returns:
            float: The calculated service rate.
        """

        balance = account.get_balance()
        service_charge = self.BASE_SERVICE_CHARGE

        if balance < self.__minimum_balance:
            service_charge = service_charge * self.SERVICE_CHARGE_PREMIUM

        return service_charge
