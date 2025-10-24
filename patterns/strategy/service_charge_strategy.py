""""
Description: A class to manage Service Charge Strategy class  objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    ServiceChargeStrategy class: Maintains service charge strategy
    data.
    """

    BASE_SERVICE_CHARGE: 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract method
        Implemented in subclass(es).
        """
        pass
