# calculates the total income
def total_income(transactions):

    income = 0

    for transaction in transactions:
        if transaction["amount"] > 0:
            income += transaction["amount"]
    return income

# calculates the total expenses
def total_expenses(transactions):

    expense = 0

    for transaction in transactions:
        if transaction["amount"] < 0:
            expense += transaction["amount"]
    return expense

# calculates balance
def balance(transactions):
    return total_income(transactions) + total_expenses(transactions)


def total_by_category(transactions, category):

    total = 0

    for transaction in transactions:
        if transaction["category"] == category:
            total += transaction["amount"]
    return total


def add_transaction(transactions, date, amount, category, account):
    new_transaction = {
        "date": date,
        "amount": amount,
        "category": category,
        "account": account
    }
    transactions.append(new_transaction)

def total_by_account(transactions, account):
    total = 0

    for transaction in transactions:
        if transaction["account"] == account:
            total += transaction["amount"]
    return total


def percent_used(transactions, category, limit):

    spent = -total_by_category(transactions, category)
    percent = spent * 100 // limit

    return percent


def check_budgets(transactions, budgets):

    for category, limit in budgets.items():
        percent = percent_used(transactions, category, limit)
        if percent >= 80:
            print(f"WARNING {category} at {percent}% of budget")

def format_money(cents):
    return f"${cents / 100:,.2f}"

def print_report(transactions, budgets):
    print("=== MONTHLY REPORT ===")
    print(f"Income: {format_money(total_income(transactions))}")
    print(f"Expenses: {format_money(total_expenses(transactions))}")
    print(f"Balance: {format_money(balance(transactions))}")

    print()
    print("---- Budget Alerts ----")
    check_budgets(transactions, budgets)



def main ():

    transactions = [
    {"date": "2026-01-03", "amount": 200000, "category": "Salario fijo", "account": "Debit"},
    {"date": "2026-01-05", "amount": -4500, "category": "Restaurants", "account": "Debit"},
    {"date": "2026-01-09", "amount": -2000, "category": "Gas", "account": "Cash"},
    {"date": "2026-01-12", "amount": -3500, "category": "Restaurants", "account": "Cash"},
    {"date": "2026-01-15", "amount": -1500, "category": "Gym", "account": "Debit"},
    ]

    budgets = {"Restaurants": 10000, "Gas": 5000, "Gym": 1500, "Travel": 20000}

    print_report(transactions, budgets)

main()













