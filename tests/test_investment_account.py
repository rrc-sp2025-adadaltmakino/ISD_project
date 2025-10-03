"""
Description: Unit tests for the InvestmentAccount class.
Author: Amanda Dadalt Makino
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""
import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        self.investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 3.0)


    def test_init_valid_inputs_attributes_set(self):
        # Arrange & Act
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 3.0)
        # Assert
        self.assertEqual(1234,
                         investment_account._BankAccount__account_number)
        self.assertEqual(4567,
                         investment_account._BankAccount__client_number)
        self.assertEqual(10000,
                         round(investment_account._BankAccount__balance, 2))
        self.assertEqual(date(2024, 11,14),
                         investment_account._date_created)
        self.assertEqual(3.0,
                         investment_account._InvestmentAccount__management_fee)


    def test_init_management_fee_invalid_type_returns_correct_fee(self):
        # Arrange & Act
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), "three")
        # Assert
        self.assertEqual(
            investment_account._InvestmentAccount__management_fee, 2.55 )


    def test_get_services_charge_date_created_more_than_10years_ago(self):
        # Arrange
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2000, 11, 14), 3.0)
        # Act
        charges = investment_account.get_service_charges()
        # Assert
        self.assertEqual(charges, 0.5)


    def test_get_services_charge_date_created_exactly_10years_ago(self):
        # Arrange
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2015, 9, 14), 3.0)
        # Act
        charges = investment_account.get_service_charges()
        # Assert
        self.assertEqual(charges, 0.5)


    def test_get_services_charge_date_created_within_10years_ago(self):
        # Arrange
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2000, 11, 14), 3.0)
        # Act
        charges = investment_account.get_service_charges()
        # Assert
        self.assertEqual(charges, 0.5)


    def test_str_displays_waived_message_when_date_more_than_10yearsago(self):
        # Arrange
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2000, 11, 14), 3.0)
        # Act
        expected = "Account Number: 1234 Balance: $10,000.00\nDate Created:" \
        " 2000-11-14 Management Fee: Waived Account Type: Investment"
        # Assert
        self.assertEqual(expected, str(investment_account))


    def test_str_displays_fee_when_date_within_10yearsago(self):
        # Arrange
        investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2020, 11, 14), 3.0)
        # Act
        expected = "Account Number: 1234 Balance: $10,000.00\nDate Created:" \
        " 2020-11-14 Management Fee: $3.00 Account Type: Investment"
        # Assert
        self.assertEqual(expected, str(investment_account))
