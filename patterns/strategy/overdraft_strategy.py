""""
Description: A class to manage Overdraft Strategy class  objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class OverdraftStrategy:
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

        Raises:

        """
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate


    def calculate_service_charges(self) -> float:
        """
        Simulates the calculation of service charges according to the 
        overdraft limit, and overdraft rate.

        Returns:
            float: The calculated service rate.
        """

        # if self.balance >= self.__overdraft_limit:
        #     return super().BASE_SERVICE_CHARGE

        # else:
        #     return (super().BASE_SERVICE_CHARGE +
        #             (self.__overdraft_limit - self.balance)
        #             * self.__overdraft_rate)