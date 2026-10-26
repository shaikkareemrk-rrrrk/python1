# Smart Electricity Billing for Multiple Apartments

# Apartment details: (Apartment, Units Consumed, Previous Bill)
apartments = [
    ("A101", 80, 300),
    ("A102", 150, 800),
    ("A103", 250, 1600),
    ("A104", 50, 250)
]

fixed_charge = 50
rebate = 20

bills = []

print("SMART ELECTRICITY BILLING")
print("-" * 40)

for apartment, units, previous_bill in apartments:

    # Progressive tariff calculation
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3
    else:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    total_bill = energy_charge + fixed_charge - rebate

    if total_bill < 0:
        total_bill = 0

    print("\nApartment:", apartment)
    print("Units consumed:", units)
    print("Energy charge:", energy_charge)
    print("Fixed charge:", fixed_charge)
    print("Rebate:", rebate)
    print("Final bill: Rs.", total_bill)

    # Detect billing discrepancy
    if abs(total_bill - previous_bill) > 100:
        print("Billing discrepancy detected!")
    else:
        print("Bill verified.")

    bills.append((apartment, units, total_bill))

# Rank apartments by consumption (highest first)
for i in range(len(bills)):
    for j in range(0, len(bills) - i - 1):
        if bills[j][1] < bills[j + 1][1]:
            bills[j], bills[j + 1] = bills[j + 1], bills[j]

print("\nAPARTMENT RANKING BY CONSUMPTION")
print("-" * 40)

rank = 1
for apartment, units, total_bill in bills:
    print("Rank:", rank, "| Apartment:", apartment,
          "| Units:", units, "| Bill: Rs.", total_bill)
    rank = rank + 1