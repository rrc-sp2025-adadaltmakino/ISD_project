"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Amanda Dadalt Makino"


# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from datetime import date
from bank_account import *


# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(1234, 4567, 100,
                                       date(2024, 11, 14), 200, 10)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
try:
    print(chequing_account)
except ValueError as e:
    print(e)

# 3b. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
try:
    print(chequing_account.get_service_charges())
except ValueError as e:
    print(e)

# 4a. Use ChequingAccount instance created in step 2 to deposit
# enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.deposit(900)
except ValueError as e:
    print(e)

# 4b. Print the ChequingAccount
try:
    print(chequing_account)
except ValueError as e:
    print(e)

# 4c. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
try:
    print(chequing_account.get_service_charges())
except ValueError as e:
    print(e)

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(1234, 4567, 10000, (2024, 11, 14), 100)
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
try:
    print(savings_account)
except ValueError as e:
    print(e)

# 6b. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
try:
    print(savings_account.get_service_charges())
except ValueError as e:
    print(e)

# 7a. Use this SavingsAccount instance created in step 5 to withdraw
# enough money from the savings account to cause the balance to fall
# below the minimum balance.
try:
    savings_account.withdraw(9950)
except ValueError as e:
    print(e)

# 7b. Print the SavingsAccount.
try:
    print(savings_account)
except ValueError as e:
    print(e)

# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
try:
    print(savings_account.get_service_charges())
except ValueError as e:
    print(e)


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your
# choice including a date created within the last 10 years.
try:
    investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2020, 11, 14), 3.0)
except ValueError as e:
    print(e)


# 9a. Print the InvestmentAccount created in step 8.
try:
    print(investment_account)
except ValueError as e:
    print(e)

# 9b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 8.
try:
    print(investment_account.get_service_charges())
except ValueError as e:
    print(e)

# 10. Create an instance of an InvestmentAccount with values of your
# choice including a date created prior to 10 years ago.
try:
    old_investment_account = InvestmentAccount(1234, 4567, 10000,
                                           date(2000, 11, 14), 3.0)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
try:
    print(old_investment_account)
except ValueError as e:
    print(e)

# 11b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 10.
try:
    print(old_investment_account.get_service_charges())
except ValueError as e:
    print(e)

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10
# by using the withdraw method of the superclass and withdrawing
# the service charges determined by each instance invoking the
# polymorphic get_service_charges method.
try:
    chequing_account.withdraw(chequing_account.get_service_charges())
except ValueError as e:
    print(e)

try:
    savings_account.withdraw(savings_account.get_service_charges())
except ValueError as e:
    print(e)

try:
    investment_account.withdraw(investment_account.get_service_charges())
except ValueError as e:
    print(e)

try:
    old_investment_account.withdraw(
        old_investment_account.get_service_charges()
        )
except ValueError as e:
    print(e)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
try:
    print(chequing_account)
except ValueError as e:
    print(e)

try:
    print(savings_account)
except ValueError as e:
    print(e)

try:
    print(investment_account)
except ValueError as e:
    print(e)

try:
    print(old_investment_account)
except ValueError as e:
    print(e)
