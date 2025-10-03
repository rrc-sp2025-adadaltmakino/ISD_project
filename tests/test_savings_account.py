"""
Description: Unit tests for the SavingsAccount class.
Author: Amanda Dadalt Makino
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""
import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        self.savings_account = SavingsAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 100)


    def test_init_valid_inputs_attributes_set(self):
        # Arrange & Act
        savings_account = SavingsAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 100)
        # Assert
        self.assertEqual(1234,
                         savings_account._BankAccount__account_number)
        self.assertEqual(4567,
                         savings_account._BankAccount__client_number)
        self.assertEqual(10000,
                         round(savings_account._BankAccount__balance, 2))
        self.assertEqual(date(2024, 11,14),
                         savings_account._date_created)
        self.assertEqual(100.0,
                         savings_account._SavingsAccount__minimum_balance)


    def test_init_minimum_balance_invalid_set_to_appropriate_value(self):
        # Arrange & Act
        savings_account = SavingsAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), "hundred")
        # Assert
        self.assertEqual(50.0, 
                         savings_account._SavingsAccount__minimum_balance)


    def test_get_services_charges_balance_greater_than_minimum_balance(self):
        # Arrange
        savings_account = SavingsAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 100)
        # Act
        charges = savings_account.get_service_charges()
        # Assert
        self.assertEqual(charges, 0.5)


    def test_get_services_charges_balance_equal_to_minimum_balance(self):
        # Arrange
        savings_account = SavingsAccount(1234, 4567, 100,
                                           date(2024, 11, 14), 100)
        # Act
        charges = savings_account.get_service_charges()
        # Assert
        self.assertEqual(charges, 0.5)


    def test_get_services_charges_balance_less_than_minimum_balance(self):
        # Arrange
        savings_account = SavingsAccount(1234, 4567, 50,
                                           date(2024, 11, 14), 100)
        # Act
        charges = savings_account.get_service_charges()
        # Assert
        self.assertEqual(charges, 1.0)


    def test_str_returns_appropriate_values(self):
        # Arrange
        savings_account = SavingsAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 100)
        # Act
        expected = "Account Number: 1234 Balance: $10,000.00\n" \
        "Minimum Balance: $100.00 Account Type: Savings"
        # Assert
        self.assertEqual(expected, str(savings_account))
