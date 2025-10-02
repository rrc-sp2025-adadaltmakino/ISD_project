"""
Description: Unit tests for the ChequingAccount class.
Author: Amanda Dadalt Makino
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""
import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.chequing_account = ChequingAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 200, 10)

    def test_init_valid_inputs_attributes_set(self):
        # Arrange & Act
        chequing_account = ChequingAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 200, 10)
        # Assert
        self.assertEqual(1234,
                         chequing_account._BankAccount__account_number)
        self.assertEqual(4567,
                         chequing_account._BankAccount__client_number)
        self.assertEqual(10000,
                         round(chequing_account._BankAccount__balance, 2))
        self.assertEqual(date(2024, 11,14),
                         chequing_account._date_created)
        self.assertEqual(200.00,
                         chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(10.00,
                         chequing_account._ChequingAccount__overdraft_rate)


    def test_init_overdraft_limit_invalid_type_sets_to_minus_a_hundred(self):
        # Arrange & Act
        chequing_account = ChequingAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), "hundred", 10)
        # Assert
        self.assertEqual(chequing_account._ChequingAccount__overdraft_limit,
                         -100)


    def test_init_overdraft_rate_invalid_type_sets_rate(self):
        # Arrange & Act
        chequing_account = ChequingAccount(1234, 4567, 10000,
                                           date(2024, 11, 14), 200, "ten")
        # Assert
        self.assertEqual(chequing_account._ChequingAccount__overdraft_rate,
                         0.05)


    def test_init_date_created_invalid_type(self):
        # Arrange & Act
        chequing_account = ChequingAccount(1234, 4567, 10000,
                                           "November 14", 200, "ten")
        # Assert
        self.assertEqual(chequing_account._date_created,
                         date.today())
