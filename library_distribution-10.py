# Multi-Criteria Library Resource Distribution

# Books: (Book Name, Available Copies)
books = [
    ("Python", 10),
    ("AI", 8),
    ("Database", 6)
]

# Branch requirements: (Branch, Book, Demand, Priority)
requirements = [
    ("Main", "Python", 5, 1),
    ("City", "Python", 4, 2),
    ("Rural", "Python", 3, 3),
    ("Main", "AI", 4, 1),
    ("City", "AI", 6, 2),
    ("Rural", "AI", 3, 3),
    ("Main", "Database", 4, 1),
    ("City", "Database", 3, 2)
]

print("LIBRARY RESOURCE DISTRIBUTION")
print("-" * 40)

total_unmet = 0

# Allocate higher-priority requirements first
for book_name, available in books:
    print("\nBook:", book_name)
    remaining = available

    # Priority 1 is highest
    for priority in range(1, 4):
        for branch, book, demand, level in requirements:
            if book == book_name and level == priority:
                allocated = min(demand, remaining)
                unmet = demand - allocated
                remaining = remaining - allocated
                total_unmet = total_unmet + unmet

                print("Branch:", branch)
                print("Demand:", demand)
                print("Allocated:", allocated)
                print("Unmet demand:", unmet)

    print("Copies remaining:", remaining)

print("\nFINAL SUMMARY")
print("-" * 40)
print("Total unmet demand:", total_unmet)