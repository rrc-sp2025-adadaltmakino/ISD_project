# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  
Each assignment will build on the work done in the previous assignment(s).  
Ultimately, an entire system will be created to manage bank transactions
for clients who have one or more bank accounts.

## Author

Amanda Dadalt Makino

## Assignment

Assignment 01: Classes

This assignment will help to reinforce learning of the Module 1 concepts of:

- Interpreting a Class Diagram
- Encapsulation
- Classes
- Unit Test Planning

Assignment 02:

This assignment will help to reinforce learning of the Module 2
concepts of:

- Abstraction
- Inheritance
- Superclass/Subclass
- Polymorphism

Assignment 03:

This assignment will help to reinforce learning of the Module 3 concepts of:

- Design Patterns
- Best Practices when Implementing Design Patterns
- Strategy Pattern
- Observer Pattern

Assignment 04:

This assignment will help to reinforce learning of the Module 4 concepts of:

- Programming Paradigms
- PySide6
- Qt Framework
- PySide6 Widgets

Assignment 05:

This assignment will help to reinforce learning of the Module 5 concepts of:

- Algorithms
- Sphinx
- Generate help files
- Creating Exe
- PyInstaller
- Inno Setup

## Encapsulation

Encapsulation was achieved by defining attributes like 'account_number',
'client_number', and 'balance' in the class BankAccount, and by defining
methods like 'update_balance()', 'deposit()', and 'withdraw()'. What also
helps with encapsulation is the use of accessors.

## Polymorphism

In the BankAccount class, polymorphism was achieved when I defined the
get_service_charges() method. I defined it in the BankAccount superclass,
and inhereted it in the InvestmentAccount, ChequingAccount, and SavingsAccount
subclasses. In the BankAccount class I just used the "pass" since there are
not enough information available at the superclass level, and when it was
inhereted in the subclasses the polymorphism was implemented by using that
method to behave different ways according to each subclass requirements.

## Strategy Pattern

The strategy pattern was implemented in my bank account classes/subclasses
by creating different strategies for each type of account. For example, the
management_fee_strategy is implementing InvestmentAccount logic to calculate
service charges. The minimum balance strategy was created focused on the
SavingsAccount logic, and so on.

## Observer Pattern

The observer pattern was implemented in the BankAccount class/subclasses when
BankAccount class became the subject and the Client class became the observer.
I used the attach() method to connect the observer to the appropriate bank
account, and the notify() method when a big event occurs (large transaction
or low balance) to automatically send a notification to the client through
their email.

## Event-Driven Programming

Event-Driven Programming was implemented in this assignment by making the
program react to events like buttons, clicks, deposit/withdraw, and signals.
It is based on user interaction, for example, when the user clicks a button
and that interaction triggers a function that will search for the client. All
of this was achieved by using programming paradigms, Qt Framework, and PySide6
along with its widgets.

## Filtering

Filtering was implemented in this assignment by setting up the program to search
for and display only the information that matches the speciific criteria. For
example, when looking up a client, the application can apply filters for their
Account number, Balance, Date created, and Account type. This was achieved by
using search functions that will scan through the CSV files and return the
appropriate data.