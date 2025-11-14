__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Amanda Dadalt Makino"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account 
    transactions.
    """

    ##Signal
    # signal_name = Signal(parameter_datatypes)
    balance_updated = Signal(BankAccount)


    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails 
        window.
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


    def __on_apply_transaction(self) -> None:
        """
        Attempt to perform a transaction (deposit or withdraw) using
        the amount entered into the corresponding bank account.
        """
        # try/except to convert amount into the widget to float -> QMsgBox
        # if the conversion fails

        amount_string = self.transaction_amount_edit.text().strip()

        try:
            amount = float(amount_string)
        except ValueError:
            QMessageBox.information(self,
                                    "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        # try/except to evaluate self.sender() wether the user clicked
        # on the deposit button or withdraw button

        sender = self.sender()
        transaction_type = ""

        try:
            if sender is self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)

            elif sender is self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            # update balance
            self.balance_label.setText(f"${self.account.balance:.2f}")

            ##Signal
            self.balance_updated.emit(self.account)

            # set transaction amount edit to an empty string and setFocus
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            QMessageBox.information(self, f"{transaction_type} Failed",
                                    str({e}))

            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()


    def __on_exit(self) -> None:
        """
        Close the QDialog returning the user to the ClientLookupWindow.
        """
        self.close()
