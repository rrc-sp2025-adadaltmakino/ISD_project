"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Amanda Dadalt Makino"


# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from datetime import date
from bank_account import *
from client import *


# 2. Create a Client object with data of your choice.

try:
    client = Client(1234, "Amanda", "Makino",
                        "amandadm@pixell-river.com")
except ValueError as e:
    print(e)


# 3a. Create a ChequingAccount object with data of your choice, using the client_number
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number
# of the client created in step 2.

try:
    chequing_account = ChequingAccount(2002, 4567, 1000,
                                       date(2024, 11, 14), 200, 10)
except ValueError as e:
    print(e)

try:
    savings_account = SavingsAccount(3003, 4567, 500, date(2024, 11, 14), 50)
except ValueError as e:
    print(e)


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount
# object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount
# object (created in step 2).

# subject.attach(observer)
try:
    chequing_account.attach(client)
except ValueError as e:
    print(e)

try:
    savings_account.attach(client)
except ValueError as e:
    print(e)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number
try:
    new_client = Client(9876, "Laurie", "Cutrone",
                            "lcutrone@pixell-river.com")
except ValueError as e:
    print(e)

try:
    new_client_savings_account = SavingsAccount(
        3004, 9876, 500, date(2022, 10, 15), 50)
except ValueError as e:
    print(e)

try:
    new_client_savings_account.attach(new_client)
except ValueError as e:
    print(e)


# 6. Use the ChequingAccount and SavingsAccount objects created
# in steps 3 and 5 above to perform transactions (deposits and withdraws)
# which would cause the Subject (BankAccount) to notify the Observer
# (Client) as well as transactions that would not
# cause the Subject to notify the Observer.  Ensure each
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such
# that any exception messages are printed to the console.

### CLIENT ###

## CHEQUING
#no notification
try:
    chequing_account.deposit(500)
except ValueError as e:
    print(e)

#low balance warning
try:
    chequing_account.withdraw(1455)
except ValueError as e:
    print(e)

#large transaction
try:
    chequing_account.deposit(20000)
except ValueError as e:
    print(e)

##SAVINGS
#no notification
try:
    savings_account.withdraw(20)
except ValueError as e:
    print(e)

#low balance warning
try:
    savings_account.withdraw(435)
except ValueError as e:
    print(e)

#large transaction
try:
    savings_account.deposit(20000)
except ValueError as e:
    print(e)


### NEW CLIENT ###

#no notification
try:
    new_client_savings_account.deposit(500)
except ValueError as e:
    print(e)

#low balance warning
try:
    new_client_savings_account.withdraw(955)
except ValueError as e:
    print(e)

#large transaction
try:
    new_client_savings_account.deposit(15000)
except ValueError as e:
    print(e)
