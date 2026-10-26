
# ATM Transaction Sequence Simulation

balance = 5000
withdrawal_limit = 2000

# Transaction sequence: (type, amount)
transactions = [
    ("Deposit", 3000),
    ("Withdraw", 1500),
    ("Withdraw", 2500),
    ("Deposit", 1000),
    ("Withdraw", 1000),
    ("Withdraw", -500)
]

deposit_count = 0
withdrawal_count = 0
rejected_count = 0
total_deposits = 0
total_withdrawals = 0

print("ATM TRANSACTION SUMMARY")
print("-" * 45)
print("Opening Balance: INR", balance)

for transaction_type, amount in transactions:

    if amount <= 0:
        print(transaction_type, amount, "- Invalid Transaction")
        rejected_count = rejected_count + 1

    elif transaction_type == "Deposit":
        balance = balance + amount
        total_deposits = total_deposits + amount
        deposit_count = deposit_count + 1
        print("Deposit: INR", amount, "- Successful")

    elif transaction_type == "Withdraw":
        if amount > withdrawal_limit:
            print("Withdraw: INR", amount, "- Limit Exceeded")
            rejected_count = rejected_count + 1

        elif amount > balance:
            print("Withdraw: INR", amount, "- Insufficient Balance")
            rejected_count = rejected_count + 1

        else:
            balance = balance - amount
            total_withdrawals = total_withdrawals + amount
            withdrawal_count = withdrawal_count + 1
            print("Withdraw: INR", amount, "- Successful")

    else:
        print(transaction_type, "- Unknown Transaction")
        rejected_count = rejected_count + 1

print("-" * 45)
print("Total Deposits: INR", total_deposits)
print("Total Withdrawals: INR", total_withdrawals)
print("Successful Deposits:", deposit_count)
print("Successful Withdrawals:", withdrawal_count)
print("Rejected Transactions:", rejected_count)
print("Final Balance: INR", balance)
