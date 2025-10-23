""""
Description: A class to manage Overdraft Strategy class  objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    OverdraftStrategy class: Maintains overdraft strategy data.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes class attributes to argument values.

        Args:
            - overdraft_limit(float): Value that represents the
            overdraft limit.
            - overdraft_rate(float): Value that represents the overdraft
            rate.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate


    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Simulates the calculation of service charges according to the 
        overdraft limit, and overdraft rate.

        Args:
            account(BankAccount): The bank account that will be used.

        Returns:
            float: The calculated service rate.
        """
        balance = account.get_balance()

        if balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return (
                self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - balance)
                * self.__overdraft_rate
            )
