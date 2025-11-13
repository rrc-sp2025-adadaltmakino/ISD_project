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

    
    @Slot
    def on_lookup_client(self) -> None:
        """
        Slot for the look_up button clicked signal,
        Displays client data on the screen.
        """
        # obtain Client object from the client_listing:dict based on
        #the client_number entered into the client_number_edit widget
        # retrieve BankAccount records associated with the Client and
        #displays details of records in the account_table

        # if no Client record matches the client_number entered
        # a QMessageBox will display 

        ## obtain client number into the client_number_edit widget 
        ## try convert to int, except issue in QMsgBox
        
        client_number_text = self.client_number_edit.text().strip()

        try:
            client_number = int(client_number_text)
        except ValueError:
            QMessageBox.information(self, "Input Error",
                                "Client Number must be a numeric value.")
            self.reset_display()
            return

        self.reset_display()


        ## check if client_number entered exists in key (client_listing)
        ## if not: display QMsgBox

        if client_number not in self.client_listing:
            QMessageBox.information(self, "Not Found", 
                                    f"Client Number: {client_number} "
                                    + "not found.")

            self.reset_display()
            return

    @Slot
    def on_text_changed(self) -> None:
        """
        
        """

    @Slot
    def on_select_account(self) -> None:
        """
        
        """
