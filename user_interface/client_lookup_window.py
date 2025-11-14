__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Amanda Dadalt Makino"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data, manage_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    ClientLookupWindow class: Maintains look up window data.
    """

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
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)


    @Slot()
    def __on_lookup_client(self) -> None:
        """
        Slot for the look_up button clicked signal,
        Displays client data on the screen.
        """

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


        ## obtain corresponding value (Client object) from the dict
        ## set the client_info_label to hte Client Name

        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client Name: {client.first_name} "
                                       +f"{client.last_name}")


        ## iterate thru the accounts dict values
        ## if client_number in Client match the one in BankAccount - add row
        # QTableWidgetItems for each of the columns
        row = 0

        for account in self.accounts.values():
            if account.client_number == client_number:
                self.account_table.insertRow(row)


                ## create QTableWidgets for each of the account table columns
                ## account number (column 0)
                account_number_item = QTableWidgetItem(str(account.account_number))
                account_number_item.setTextAlignment(Qt.AlignCenter)

                ## balance (column 1)
                balance_item_string = f"${account.balance:.2f}"
                balance_item = QTableWidgetItem(balance_item_string)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                ## date created (column 2)
                date_created_item = QTableWidgetItem(str(account._date_created))
                date_created_item.setTextAlignment(Qt.AlignCenter)

                ## account type (column 3)
                account_type_item = QTableWidgetItem(account.__class__.__name__)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                ## place items in table
                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)

                row += 1

        self.account_table.resizeColumnsToContents()


    @Slot()
    def __on_text_changed(self) -> None:
        """
        Clear all bank account records from display.
        """
        ## use setRowCount w an argument of 0
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Identify the account selected and transfer control to the
        Account Details window.

        Args:
            row(int): Row of the clicked cell
            column(int): Column  of the clicked cell
        """

        ERRORS = {
            "invalid": ("Invalid Selection", 
                        "Please select a valid record."),
            "no_account": ("No Bank Account", 
                           "Bank Account selected does not exist.")
        }

        error_title = None
        error_message = None

        selected_item = self.account_table.item(row, 0)

        if selected_item is None:
            error_title, error_message = ERRORS["invalid"]

        else:
            account_text = selected_item.text().strip()

            if account_text == "":
                error_title, error_message = ERRORS["no_account"]

            else:
                try:
                    account_number = int(account_text)
                except ValueError:
                    error_title, error_message = ERRORS["invalid"]

                else:
                    if account_number in self.accounts:
                        account_object = self.accounts[account_number]

                        details_window = AccountDetailsWindow(account_object)

                        # CONNECT SIGNAL
                        details_window.balance_updated.connect(
                            self.updated_data)

                        details_window.exec()

                        return
                    else:
                        error_title, error_message = ERRORS["no_account"]

        if error_title:
            QMessageBox.information(self, error_title, error_message)

    @Slot()
    def __update_data(self, account: BankAccount):
        """
        Update bank account balance according to the value when
        receiving a signal from AccountDetailsWindow.

        Args:
            account(BankAccount): Client's bank account.
        """

        for row in range(self.account_table.rowCount()):

            # value text of first column in the iteration
            row_account_number = int(self.account_table.item(row, 0).text())

            # compare account number with row account number (if they match)
            if row_account_number == account.account_number:
                # update the value of the second column
                self.account_table.setItem(
                    row, 1, QTableWidgetItem(f"${account.balance:.2f}")
                )

        self.accounts[account.account_number] = account

        manage_data.update_data(account)
