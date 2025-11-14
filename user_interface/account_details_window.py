__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if not isinstance(account, BankAccount):
            self.reject()
            return

        # set account attribute to a copy of the received parameter value
        self.account = copy.copy(account)

        # setText to populate account number label and balance label + format
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"${self.account.balance:.2f}")

        # connection signals
        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)


    def __on_apply_transaction(self):
        pass

    def __on_exit(self):
        pass
