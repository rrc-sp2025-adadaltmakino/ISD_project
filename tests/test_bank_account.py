"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest

from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(1234, 4567, 10000)

    def test_init_valid_inputs_attributes_set(self):
        # Arrange & Act
        bank_account = BankAccount(1234, 4567, 10000)

        # Assert
        self.assertEqual(1234, bank_account._BankAccount__account_number)
        self.assertEqual(4567, bank_account._BankAccount__client_number)
        self.assertEqual(10000, round(bank_account._BankAccount__balance, 2))


    def test_init_non_numeric_balance_set_balance_to_zero(self):
        # Arrange & Act
        bank_account = BankAccount(1234, 4567, " ")

        # Assert
        self.assertEqual(round(bank_account._BankAccount__balance, 2), 0)


    def test_init_non_numeric_accountnumber_raises_valueerror(self):
        # Arrange, Act, and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("number", 4567, 10000)


    def test_init_clientnumber_raises_valueerror(self):
        # Arrange, Act, and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(1234, "number", 10000)


    def test_accountnumber_getter_returns_accountnumber(self):
        # Arrange, Act, and Assert
        self.assertEqual(1234, self.bank_account.account_number)


    def test_clientnumber_getter_returns_clientnumber(self):
        # Arrange, Act, and Assert
        self.assertEqual(4567, self.bank_account.client_number)


    def test_balance_getter_returns_balance(self):
        # Arrange, Act, and Assert
        self.assertEqual(10000, round(self.bank_account.balance, 2))


    def test_update_balance_updates_balance_using_positive_amount(self):
        # Arrange & Act
        self.bank_account.update_balance(500)

        # Assert
        self.assertEqual(10500, round(self.bank_account.balance, 2))


    def test_update_balance_updates_balance_using_negative_amount(self):
        # Arrange & Act
        self.bank_account.update_balance(-500)

        # Assert
        self.assertEqual(9500, round(self.bank_account.balance, 2))


    def test_update_balance_remains_unchange_using_invalid_amount(self):
        # Arrange & Act
        self.bank_account.update_balance("twenty")

        # Assert
        self.assertEqual(10000, round(self.bank_account.balance, 2))


    def test_deposit_updating_balance_when_valid_amount_provided(self):
        # Arrange & Act
        self.bank_account.deposit(500)

        # Assert
        self.assertEqual(10500, round(self.bank_account.balance, 2))


    def test_deposit_raise_valueerror_when_negative_amount_provided(self):
        # Arrange, Act, and Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-500)


    def test_withdraw_updates_balance_valid_amount(self):
        # Arrange & Act
        self.bank_account.withdraw(500)

        # Assert
        self.assertEqual(9500, round(self.bank_account.balance, 2))


    def test_withdraw_raises_valueerror_with_negative_amount(self):
        # Arrange, Act, and Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-500)


    def test_withdraw_raises_valueerror_with_exceeding_amount(self):
        # Arrange, Act, and Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(50000)


    def test_str_valid_instance_returns_formatted_string(self):
        expected = "Account Number: 1234 Balance: $10000.00"

        self.assertEqual(expected, str(self.bank_account))
