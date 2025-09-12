"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest

from client.client import Client
from email_validator import validate_email, EmailNotValidError

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1234, "Amanda", "Makino", 
                             "amandadm@pixell-river.com")

    def test_init_valid_inputs_attributes_set(self):
        # Arrange & Act
        self.assertEqual(1234, self.client.client_number)
        self.assertEqual("Amanda", self.client.first_name)
        self.assertEqual("Makino", self.client.last_name)
        self.assertEqual("amandadm@pixell-river.com",
                         self.client.email_address)


    def test_init_blank_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client("", "Amanda", "Makino", 
                            "amandadm@pixell-river.com")

    def test_init_blank_first_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client(1234, " ", "Makino",
                            "amandadm@pixell-river.com")

    def test_init_blank_last_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            client = Client(1234, "Amanda", " ",
                            "amandadm@pixell-river.com")

    def test_init_invalid_email_address(self):
        # Arrange, Act
        client = Client(1234, "Amanda", "Makino", "amandadm")

        # Assert
        self.assertEqual(
            client.email_address, "amandadm@pixell-river.com"
            )

    def test_client_number_accessor_returns_client_number(self):
        self.assertEqual(1234, self.client.client_number)

    def test_first_name_accessor_returns_client_first_name(self):
        self.assertEqual("Amanda", self.client.first_name)

    def test_last_name_accessor_returns_last_name(self):
        self.assertEqual("Makino", self.client.last_name)

    def test_email_address_accessor_returns_email_address(self):
        self.assertEqual("amandadm@pixell-river.com",
                        self.client.email_address)

    def test_str_valid_instance_returns_formatted_string(self):
        expected = (
            "Makino, Amanda [1234] - amandadm@pixell-river.com"
        )

        self.assertEqual(expected, str(self.client))
