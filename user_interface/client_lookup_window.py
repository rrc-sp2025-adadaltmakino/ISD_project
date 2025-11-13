__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Amanda Dadalt Makino"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    
    def __init__(self):
        """
        Initializes class attributes to argument values.
        """
        super().__init__()

        # call load_data() and set attribute to the value
        client_listing, accounts = load_data()
        self.client_listing = client_listing
        self.accounts = accounts

        # establishing connnections
        self.lookup_button.clicked.connect(self.on_lookup_client) #lookup_button - clicked - lookup_client()
        self.client_number_edit.textChanged.connect(self.on_text_changed) #client_number_edit - textChanged - on_text_changed()
        self.account_table.cellClicked.connect(self.on_select_account) #account_table - cellClicked - on_select_account()
