"""
Package initialization.
"""

__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from client.client import Client
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from patterns.strategy.overdraft_strategy import OverdraftStrategy
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from .bank_account import BankAccount
from .chequing_account import ChequingAccount
from .investment_account import InvestmentAccount
from .savings_account import SavingsAccount

__all__ = ["BankAccount", "ChequingAccount", "InvestmentAccount",
           "SavingsAccount", "Client", "ManagementFeeStrategy", 
           "MinimumBalanceStrategy", "OverdraftStrategy", 
           "ServiceChargeStrategy"]
