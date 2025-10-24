""""
Description: A class to manage ManagementFeeStrategy class objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    ManagementFeeStrategy class: Maintains management fee strategy 
    data.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes class attributes to argument values.

        Args:
            - date_created(date): The date the account was created.
            - management_fee(float): The management fee amount applied.
        """

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Simulates the get service charges process according to the 
        date created.

        Returns:
            float: The calculated service rate.
        """

        service_charge = self.BASE_SERVICE_CHARGE

        if self.__date_created > self.TEN_YEARS_AGO:
            service_charge += self.__management_fee

        return service_charge
