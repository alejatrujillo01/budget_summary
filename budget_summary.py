transactions = [
    {"date": "2026-01-03", "amount": 200000, "category": "Salario fijo", "account": "Debit"},
    {"date": "2026-01-05", "amount": -4500, "category": "Restaurants", "account": "Debit"},
    {"date": "2026-01-09", "amount": -2000, "category": "Gas", "account": "Cash"},
    {"date": "2026-01-12", "amount": -3500, "category": "Restaurants", "account": "Cash"},
    {"date": "2026-01-15", "amount": -1500, "category": "Gym", "account": "Debit"},
]

budgets = {"Restaurants": 10000, "Gas": 5000, "Gym": 1500, "Travel": 20000}

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



# print(total_income(transactions))
# print(total_expenses(transactions))
# print(balance(transactions))
# print(total_by_category(transactions, "Restaurants"))


# print(total_by_account(transactions, "Cash"))     # -5500
# print(total_by_account(transactions, "Debit"))    # 194000

# print(len(transactions))                          # 5
# add_transaction(transactions, "2026-01-20", -2500, "Gas", "Cash")
# print(len(transactions))                          # 6
# print(balance(transactions))                      # 186000

# print(percent_used(transactions, "Restaurants", 10000))
# check_budgets(transactions, budgets)















