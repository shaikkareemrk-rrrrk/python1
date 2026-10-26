
# Multi-Currency Travel Budget Analysis

budget = 50000

# Currency rates: [currency, exchange rate, fee percentage]
rates = [
    ["USD", 84, 2],
    ["EUR", 92, 1.5],
    ["GBP", 110, 2],
    ["INR", 1, 0]
]

# Expenses: (category, amount, currency)
expenses = [
    ("Hotel", 300, "USD"),
    ("Food", 120, "EUR"),
    ("Transport", 100, "GBP"),
    ("Shopping", 8000, "INR")
]

total_cost = 0
largest_cost = 0
largest_category = ""

print("MULTI-CURRENCY TRAVEL BUDGET")
print("-" * 45)

for category, amount, currency in expenses:
    for code, rate, fee_percent in rates:
        if currency == code:
            converted = amount * rate
            fee = converted * fee_percent / 100
            final_cost = converted + fee
            break

    total_cost = total_cost + final_cost

    print("\nCategory:", category)
    print("Currency:", currency)
    print("Original Amount:", amount)
    print("Converted Amount:", round(converted, 2))
    print("Conversion Fee:", round(fee, 2))
    print("Final Cost: INR", round(final_cost, 2))

    if final_cost > largest_cost:
        largest_cost = final_cost
        largest_category = category

print("\n" + "-" * 45)
print("Total Travel Cost: INR", round(total_cost, 2))
print("Planned Budget: INR", budget)
print("Largest Expense:", largest_category)

if total_cost > budget:
    print("Status: Over Budget")
    print("Extra Spending: INR", round(total_cost - budget, 2))
elif total_cost < budget:
    print("Status: Within Budget")
    print("Money Remaining: INR", round(budget - total_cost, 2))
else:
    print("Status: Budget Exactly Used")