""""
Description: A class to manage Bank Account objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"


class BankAccount:
    """
    BankAccount class: Maintains bank account data.
    """
    def __init__(self, account_number: int, client_number: int,
                 balance: float):
        """
        Initializes class attributes to argument values.

        Args:
            account_number(int):  An integer value representing the 
            bank account number.
            client_number(int):  An integer value representing the 
            client number representing the account holder.
            balance(float): A float value representing the current 
            balance of the bank account.
        
        Raises:
            ValueError: If account number is not an integer, if client
            number is not an integer, and if balance is not a float
            and cannot be transferred to a float.

        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")

        if isinstance (balance, float):
            self.__balance = balance
        else:
            try:
                self.__balance = float(balance)
            except ValueError:
                self.__balance = 0.0

    @property
    def account_number(self) -> int:
        """
        Accessor for the account number attribute.

        Returns:
            int: An integer value representing the 
            client number representing the account holder.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: An integer value representing the client number 
            representing the account holder.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute.

        Returns:
            float: A float value representing the current balance of 
            the bank account
        """
        return self.__balance

    def update_balance(self, amount: float) -> None:
        """
        Updates the balance according to the amount.

        Args:
            amount(float): The value that is going be applied to
            the balance.
        """

        valid = True

        try:
            amount = float(amount)
        except ValueError:
            valid = False

        if valid:
            self.__balance += amount


    def deposit(self, amount: float) -> None:
        """
        Simulates the deposit according to the amount value.

        Args:
            amount(float): The value that is going be added to the 
            balance.
        
        Raises:
            ValueError: If amount is not numeric, and if amount is not
            positive.
        """

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(
                f"Deposit amount: {amount} must be numeric."
                )

        if amount <= 0:
            raise ValueError(
                f"Deposit amount: ${amount:.2f} must be positive."
                )

        self.update_balance(amount)


    def withdraw(self, amount: float) -> None:
        """
        Simulates the withdrawal process according to the amount value.

        Args:
            amount(float): The value that is going be subtracted off 
            the balance.
        
        Raises:
            ValueError: if amount is not numeric, and if amount is
            negative, and if amount exceeds the current balance.
        """

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(
                f"Withdraw amount: {amount} must be numeric."
                )

        if amount <= 0:
            raise ValueError(
                f"Withdraw amount: ${amount:.2f} must be positive."
                )

        if amount > self.__balance:
            raise ValueError(
                f"Withdraw amount: ${amount:.2f} must not exceed the "
                f"account balance: ${self.__balance:.2f}"
            )

        self.update_balance(-amount)


    def __str__(self):
        """
        Returns a string representation of the class instance.

        Returns:
            str: The course instance formatted as a string.
        """

        return (
            f"Account Number: {self.__account_number} "
            f"Balance: ${self.__balance:.2f}\n"
            )
