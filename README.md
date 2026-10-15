Budget Summary

A small command-line Python program that totals income and expenses, prints a monthly report, and warns you when a spending category is close to its budget limit.

Built as a hands-on practice project to apply Python fundamentals: lists, dictionaries, functions, and loops.

Features

Calculates total income, total expenses, and balance
Totals spending by category and by account
Adds new transactions to the list
Prints a formatted monthly report
Warns when a category reaches 80% or more of its monthly budget

Example output

===== MONTHLY REPORT =====
Income:   $2,000.00
Expenses: $-115.00
Balance:  $1,885.00

----- Budget alerts -----
WARNING: Restaurants at 80% of budget
WARNING: Gym at 100% of budget

How to run
Requirements: Python 3.9 or higher. No external packages needed.
git clone https://github.com/YOUR_USERNAME/budget-summary.git
cd budget-summary
python main.py

How it works

Transactions are stored as a list of dictionaries, each with a date, amount, category, and account.
Money is stored in cents (integers) to avoid decimal rounding errors, and converted to dollars only when displayed.
Income is positive and expenses are negative, so a single sum gives the balance.
Budgets are a dictionary mapping each category to its monthly limit in cents.

Main functions
Function	                                             What it does
total_income(transactions)	                    Sum of all positive amounts
total_expenses(transactions)	                Sum of all negative amounts
balance(transactions)	                        Income plus expenses
total_by_category(transactions, category)	    Sum for one category
total_by_account(transactions, account)	        Sum for one account
add_transaction(...)	                        Adds a new transaction to the list
percent_used(transactions, category, limit)	    Percent of a budget already spent
check_budgets(transactions, budgets)	        Prints a warning at 80% or more
print_report(transactions, budgets)            	Prints the full monthly report

Project structure
budget-summary/
├── main.py
└── README.md

What I practiced
Working with lists and dictionaries together
Writing small functions that each do one job and reuse each other
Looping over lists and dictionaries (for, .items())
Avoiding bugs: integer math (//), loop placement, return vs print
Git workflow: small commits per feature, pushing to GitHub

Known limitations
Data lives in the code and is lost when the program ends
A budget limit of 0 causes a division-by-zero error (to be fixed with error handling)
Single month only, no date filtering

Author
Alejandra Trujillo, software development student. GitHub
